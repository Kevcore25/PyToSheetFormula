VERSION = 1.0

"""
Decompiles a Google Sheets formula into Python code which compiler.py (PyToSheetFormula) can compile back.

Example:
    =IF(A1>5,SUM(A1:B2),"no")
becomes
    from syntax import *

    if A1 > 5:
        SUM(A1 | B2)
    else:
        'no'

Anything that has no Python equivalent (array literals, error values, etc.) is kept as raw formula text with STR().
"""

import ast, keyword, re
from dataclasses import dataclass
from typing import *

""" CONFIG """

# When turned on, a top-level IF() becomes an if/elif/else statement (nested IFs become `x if cond else y`).
# Otherwise, every IF() becomes `x if cond else y`.
IF_AS_STATEMENT = True

# When turned on, a top-level LET() becomes variable assignments (matching compiler.py's VAR_AS_LET option).
# Otherwise, it stays as a LET() call.
LET_AS_ASSIGNMENTS = True

# When turned on, AND(), OR() and NOT() become Python's `and`, `or` and `not`.
BOOL_AS_KEYWORDS = True


""" END OF CONFIG """


class FormulaSyntaxError(ValueError):
    """Raised when a formula cannot be parsed"""

    def __init__(self, message: str, formula: str, position: int):
        self.position = position
        super().__init__(f"{message} at position {position + 1}:\n    {formula}\n    {' ' * position}^")


@dataclass
class Token:
    kind: Literal['STRING', 'NUMBER', 'REF', 'IDENT', 'RAW', 'OP', 'PUNCT', 'END']
    text: str
    start: int
    end: int
    # For REF tokens
    sheet: Optional[str] = None


# Cell references. Columns and rows on their own are only references when part of a range (e.g. A:A, 1:1)
_CELL = r'\$?[A-Za-z]{1,3}\$?\d+'
_COL = r'\$?[A-Za-z]{1,3}'
_ROW = r'\$?\d+'
_REF_BODY = rf'(?:{_CELL}(?::(?:{_CELL}|{_COL}))?|{_COL}:(?:{_CELL}|{_COL})|{_ROW}:{_ROW})'
# A reference must not run into a name or a function call (e.g. LOG10( is a function, not cell LOG10)
_REF_END = r'(?![A-Za-z0-9_.(!])'

TOKEN_PATTERNS: list[tuple[str, re.Pattern]] = [
    ('STRING', re.compile(r'"(?:[^"]|"")*"')),
    ('SHEETREF', re.compile(rf"(?P<sheet>'(?:[^']|'')+'|[A-Za-z_][A-Za-z0-9_.]*)!(?P<ref>{_REF_BODY}){_REF_END}")),
    ('REF', re.compile(rf'{_REF_BODY}{_REF_END}')),
    ('NUMBER', re.compile(r'(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?')),
    ('ERROR', re.compile(r'#(?:NULL!|DIV/0!|VALUE!|REF!|NAME\?|NUM!|N/A|ERROR!|SPILL!|CALC!|GETTING_DATA)', re.IGNORECASE)),
    ('IDENT', re.compile(r'[A-Za-z_\\][A-Za-z0-9_.]*')),
    ('OP', re.compile(r'<>|<=|>=|!=|[-+*/^&%=<>:]')),
    ('PUNCT', re.compile(r'[(),;]')),
]

# Binary operators: Sheets precedence (higher binds tighter) and their Python equivalent
COMPARE_OPS = {'=': ast.Eq, '<>': ast.NotEq, '!=': ast.NotEq, '<': ast.Lt, '<=': ast.LtE, '>': ast.Gt, '>=': ast.GtE}
BINARY_OPS = {'&': ast.BitAnd, '+': ast.Add, '-': ast.Sub, '*': ast.Mult, '/': ast.Div, '^': ast.Pow}
PRECEDENCE = {**{op: 1 for op in COMPARE_OPS}, '&': 2, '+': 3, '-': 3, '*': 4, '/': 4, '^': 5}

# Sheets function names which compiler.py spells differently
FUNCTION_RENAMES = {'CELL': 'CELLINFO'}


def call(name: str, *args: ast.expr) -> ast.Call:
    return ast.Call(func=ast.Name(id=name, ctx=ast.Load()), args=list(args), keywords=[])


def is_valid_name(name: str) -> bool:
    return name.isidentifier() and not keyword.iskeyword(name)


class SheetFormulaToPy:
    """
    Converts a Google Sheet formula into Python code (the reverse of PyToSheetFormula)
    """

    def __init__(self, formula: str):
        self.formula = formula
        self.source = ''
        self.tokens: list[Token] = []
        self.pos = 0

    """ Tokenizer """

    def tokenize(self, source: str) -> list[Token]:
        tokens = []
        i = 0
        while i < len(source):
            if source[i].isspace():
                i += 1
                continue

            # Array literals are kept as raw text
            if source[i] == '{':
                end = self.find_closing_brace(source, i)
                tokens.append(Token('RAW', source[i:end], i, end))
                i = end
                continue

            for kind, pattern in TOKEN_PATTERNS:
                match = pattern.match(source, i)
                if not match:
                    continue

                text = match.group()
                if kind == 'SHEETREF':
                    sheet = match.group('sheet')
                    if sheet.startswith("'"):
                        sheet = sheet[1:-1].replace("''", "'")
                    tokens.append(Token('REF', match.group('ref'), i, match.end(), sheet))
                elif kind == 'ERROR':
                    tokens.append(Token('RAW', text.upper(), i, match.end()))
                else:
                    tokens.append(Token(kind, text, i, match.end()))
                i = match.end()
                break
            else:
                raise FormulaSyntaxError(f"Unexpected character '{source[i]}'", source, i)

        tokens.append(Token('END', '', len(source), len(source)))
        return tokens

    def find_closing_brace(self, source: str, start: int) -> int:
        """Returns the index after the } matching the { at start, skipping over strings"""
        inStr = False
        for i in range(start + 1, len(source)):
            if source[i] == '"':
                inStr = not inStr
            elif source[i] == '}' and not inStr:
                return i + 1
        raise FormulaSyntaxError("Array literal is never closed", source, start)

    """ Parser helpers """

    @property
    def current(self) -> Token:
        return self.tokens[self.pos]

    def peek(self, offset: int = 1) -> Token:
        return self.tokens[min(self.pos + offset, len(self.tokens) - 1)]

    def advance(self) -> Token:
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def is_token(self, kind: str, text: str = None, token: Token = None) -> bool:
        token = token or self.current
        return token.kind == kind and (text is None or token.text == text)

    def expect(self, kind: str, text: str = None) -> Token:
        if not self.is_token(kind, text):
            found = self.current.text or 'end of formula'
            raise FormulaSyntaxError(f"Expected '{text or kind}' but found '{found}'", self.source, self.current.start)
        return self.advance()

    def raw(self, start: int, end: int) -> ast.Call:
        """Keeps a part of the formula as raw text, which compiles back unchanged"""
        return call('STR', ast.Constant(self.source[start:end].strip()))

    """ Parser """

    def parse_expression(self, minPrecedence: int = 1) -> ast.expr:
        """Precedence climbing over Sheets binary operators (all left-associative)"""
        left = self.parse_unary()

        while self.is_token('OP') and PRECEDENCE.get(self.current.text, 0) >= minPrecedence:
            op = self.advance().text
            right = self.parse_expression(PRECEDENCE[op] + 1)

            if op in COMPARE_OPS:
                left = ast.Compare(left=left, ops=[COMPARE_OPS[op]()], comparators=[right])
            else:
                left = ast.BinOp(left=left, op=BINARY_OPS[op](), right=right)

        return left

    def parse_unary(self) -> ast.expr:
        """Unary +/- bind tighter than ^ in Sheets (-2^2 is 4)"""
        if self.is_token('OP', '-') or self.is_token('OP', '+'):
            op = ast.USub() if self.advance().text == '-' else ast.UAdd()
            return ast.UnaryOp(op=op, operand=self.parse_unary())
        return self.parse_postfix()

    def parse_postfix(self) -> ast.expr:
        """Handles ranges (:), the tightest operator, then percentages (%)"""
        value = self.parse_primary()

        while self.is_token('OP', ':'):
            self.advance()
            value = ast.BinOp(left=value, op=ast.BitOr(), right=self.parse_primary())

        while self.is_token('OP', '%'):
            self.advance()
            value = ast.BinOp(left=value, op=ast.Div(), right=ast.Constant(100))

        return value

    def parse_primary(self) -> ast.expr:
        token = self.current

        if token.kind == 'STRING':
            self.advance()
            return ast.Constant(token.text[1:-1].replace('""', '"'))

        if token.kind == 'NUMBER':
            self.advance()
            try:
                return ast.Constant(int(token.text))
            except ValueError:
                return ast.Constant(float(token.text))

        if token.kind == 'REF':
            self.advance()
            return self.convert_ref(token)

        if token.kind == 'RAW':
            self.advance()
            return call('STR', ast.Constant(token.text))

        if self.is_token('PUNCT', '('):
            self.advance()
            value = self.parse_expression()
            self.expect('PUNCT', ')')
            return value

        if token.kind == 'IDENT':
            if self.is_token('PUNCT', '(', self.peek()):
                return self.parse_function()

            self.advance()
            if token.text.upper() in ('TRUE', 'FALSE'):
                return ast.Constant(token.text.upper() == 'TRUE')
            if is_valid_name(token.text):
                return ast.Name(id=token.text, ctx=ast.Load())
            return self.raw(token.start, token.end)

        found = token.text or 'end of formula'
        raise FormulaSyntaxError(f"Unexpected '{found}'", self.source, token.start)

    def parse_function(self) -> ast.expr:
        nameToken = self.advance()
        self.expect('PUNCT', '(')

        args: list[Optional[ast.expr]] = []
        if not self.is_token('PUNCT', ')'):
            while True:
                # Empty arguments (e.g. F(a,,b)) are kept as None
                if self.is_token('PUNCT', ',') or self.is_token('PUNCT', ';') or self.is_token('PUNCT', ')'):
                    args.append(None)
                else:
                    args.append(self.parse_expression())

                if self.is_token('PUNCT', ',') or self.is_token('PUNCT', ';'):
                    self.advance()
                    continue
                break
        self.expect('PUNCT', ')')

        # Calling a result directly, e.g. LAMBDA(x, x+1)(3), has no Python equivalent
        if self.is_token('PUNCT', '('):
            self.advance()
            depth = 1
            while depth:
                if self.is_token('END'):
                    raise FormulaSyntaxError("Bracket is never closed", self.source, self.current.start)
                if self.is_token('PUNCT', '('): depth += 1
                elif self.is_token('PUNCT', ')'): depth -= 1
                self.advance()
            return self.raw(nameToken.start, self.tokens[self.pos - 1].end)

        return self.convert_function(nameToken, args, self.tokens[self.pos - 1].end)

    """ Conversions """

    def convert_ref(self, token: Token) -> ast.expr:
        ref = token.text.upper()

        # References to other sheets
        if token.sheet is not None:
            return call('CELLREF', ast.Constant(token.sheet), ast.Constant(ref))

        # Absolute references
        if '$' in ref:
            return call('CELL', ast.Constant(ref))

        # Plain cells and ranges (A1:B2 -> A1 | B2, 1:1 -> 1 | 1)
        parts = []
        for part in ref.split(':'):
            parts.append(ast.Constant(int(part)) if part.isdigit() else ast.Name(id=part, ctx=ast.Load()))

        if len(parts) == 1:
            return parts[0]
        return ast.BinOp(left=parts[0], op=ast.BitOr(), right=parts[1])

    def convert_function(self, nameToken: Token, args: list[Optional[ast.expr]], end: int) -> ast.expr:
        name = nameToken.text.upper()

        # LET may have an empty name slot (e.g. LET(,x)), which is dropped
        if name == 'LET':
            args = [a for i, a in enumerate(args) if not (a is None and i < len(args) - 1)]

        # Other empty arguments have no Python equivalent
        if any(a is None for a in args):
            return self.raw(nameToken.start, end)

        if name == 'IF' and len(args) == 3:
            return ast.IfExp(test=args[0], body=args[1], orelse=args[2])

        if BOOL_AS_KEYWORDS:
            if name in ('AND', 'OR') and len(args) >= 2:
                return ast.BoolOp(op=ast.And() if name == 'AND' else ast.Or(), values=args)
            if name == 'NOT' and len(args) == 1:
                return ast.UnaryOp(op=ast.Not(), operand=args[0])

        pyName = FUNCTION_RENAMES.get(name, name).replace('.', '_')
        if not is_valid_name(pyName):
            return self.raw(nameToken.start, end)

        return call(pyName, *args)

    def to_statements(self, value: ast.expr, topLevel: bool = True) -> list[ast.stmt]:
        """Converts the top-level value into statements (LET -> assignments, IF -> if/elif/else)"""
        statements: list[ast.stmt] = []

        # Top-level LET: LET(name1, value1, ..., result)
        if (topLevel and LET_AS_ASSIGNMENTS and isinstance(value, ast.Call) and value.func.id == 'LET'
                and len(value.args) % 2 == 1 and all(isinstance(n, ast.Name) for n in value.args[:-1:2])):
            for name, expr in zip(value.args[:-1:2], value.args[1:-1:2]):
                statements.append(ast.Assign(targets=[ast.Name(id=name.id, ctx=ast.Store())], value=expr))
            value = value.args[-1]

        if IF_AS_STATEMENT and isinstance(value, ast.IfExp):
            statements.append(ast.If(
                test=value.test,
                body=self.to_statements(value.body, False),
                orelse=self.to_statements(value.orelse, False),
            ))
        else:
            statements.append(ast.Expr(value))

        return statements

    """ Build """

    def parse(self) -> ast.expr:
        """Parses the formula into a Python expression tree"""
        self.source = self.formula.strip()
        if self.source.startswith('='):
            self.source = self.source[1:]

        self.tokens = self.tokenize(self.source)
        self.pos = 0

        if self.is_token('END'):
            return ast.Constant('')

        value = self.parse_expression()
        if not self.is_token('END'):
            raise FormulaSyntaxError(f"Unexpected '{self.current.text}'", self.source, self.current.start)
        return value

    def build(self) -> str:
        """Starts the decompile process and returns the Python code"""
        importSyntax = ast.ImportFrom(module='syntax', names=[ast.alias(name='*')], level=0)
        module = ast.Module(body=[importSyntax, *self.to_statements(self.parse())], type_ignores=[])
        ast.fix_missing_locations(module)

        code = ast.unparse(module)
        # Blank line after the import, like code.py
        return code.replace('from syntax import *\n', 'from syntax import *\n\n', 1) + '\n'


if "__main__" in __name__:

    formula = ''
    print(SheetFormulaToPy(formula).build())
