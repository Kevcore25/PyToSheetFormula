import ast, logging, time
from typing import *

""" CONFIG """

# Turn on debug mode, which prints some messages for developing
DEBUG = False

# When turned on, if multiple expressions exist, it will choose the first expression which is non-empty and not false. 
# Otherwise, it will default to choosing the last expression used.
# Regardless of this option, a warning will be displayed if multiple values exist.
USE_FIRST_VALID = True

# In Google sheets, numbers, even if they are text, are numbers.
# This converts all user-defined strings (e.g. "123", "-1234.5") automatically into numbers if possible.
# This also saves characters, but may cause some issues on certain functions.
# When possible, this should be ideally turned on as some built-in attribute functions are designed with this in mind.
CONVERT_NUM_TO_STR = True

# Google Sheet uses indexes that start at 1 instead of 0
# When this option is turned on, any built-in function that returns an index (e.g. .index) will use Google Sheet's format instead of Python's.
# When turned off, returns will be adjusted to use Python's format (for niche scenarios).
# For compatability with pre-built functions, this option is defaulted to True but may cause some confusion.
RETURN_SHEET_INDEXES = True

# Like above, Python and Google Sheets uses different indexing systems.
# When turned on, all user-defined indexes will be adjusted to the Google Sheet system.
# By default to prevent confusion, this option is turned off.
# Note that when turned on, it may cause issues with negative indices (e.g. A1[1:-1] is now A1[0:-2] and A1[0] is now A1[-1]) 
USE_SHEET_INDEXES = False

# Character for empty
EMPTY = '""'

""" END OF CONFIG """

logging.basicConfig()
log = logging.getLogger()

if DEBUG:
    log.setLevel(logging.DEBUG)
def convert_condition_astobj(op: ast.operator) -> str:
    """
    Converts an ast object of an operator type (e.g. <) into its string value
    """
    if isinstance(op, ast.Lt): return '<'
    elif isinstance(op, ast.LtE): return '<='
    elif isinstance(op, ast.Gt): return '>'
    elif isinstance(op, ast.GtE): return '>='
    elif isinstance(op, ast.NotEq): return '!='
    elif isinstance(op, ast.Eq): return '='

    elif isinstance(op, ast.Add): return '+'
    elif isinstance(op, ast.Sub): return '-'
    elif isinstance(op, ast.Mult): return '*'
    elif isinstance(op, ast.Div): return '/'
    elif isinstance(op, ast.Mod): return '%'

    elif isinstance(op, ast.BitOr): return ':'
    elif isinstance(op, ast.BitAnd): return '&'
    elif isinstance(op, ast.BitXor): return '^'

# Compile functions
FUNCTIONS: dict[str, dict[str, ast.arg]] = {}

try:
    with open('functions.py', 'r') as f:
        for expr in ast.parse(f.read()).body:
            if isinstance(expr, ast.FunctionDef):
                args = {}
                optcount = 0
                for arg in expr.args.args:
                    args[arg.arg] = arg
                    if isinstance(arg.annotation, ast.Subscript) and arg.annotation.value.id == 'Optional':
                        optcount += 1  

                args['$count'] = len(expr.args.args)
                args['$optcount'] = len(expr.args.args) - optcount

                FUNCTIONS[expr.name] = args
except Exception as e:
    log.error(f"An error occurred while compiling functions: {e}\nPre-built functions may not be available")

class PyToSheetFormula:
    """
    Converts Python code (specifically, expressions) into a Google Sheet formula
    """
    
    def __init__(self, code: str):
        self.code = code

        self.currentFormula: str = ""
        self.finalFormulas: list[str] = []

        self.labels = {}
        self.warnings = []
        self.vars = {}
        self.debugLogs = []
        self.level = 0
        self.ERROR_THRESHOLD = 1

    def warn(self, message: str):
        self.warnings.append(message)

        
    def convert_indices(self, value: str, start: str = None, end: str = None):
        """Converts indices into a MID() format"""
        if start.isdigit():
            start = int(start)
            if USE_SHEET_INDEXES:
                start -= 1
        if end.isdigit():
            end = int(end)
            if USE_SHEET_INDEXES:
                end -= 1

        self.level += 1
        self.debug(f"Convert indice string: {value}[{start}:{end}]", 'code', 'getindex')

        LEN_TEXT = f"LEN({value})"

        if start is None:
            p_start = "1"
        elif isinstance(start, int):
            p_start = str(start + 1) if start >= 0 else f"{LEN_TEXT} {start + 1:+d}".replace("+0", "")
        else:
            p_start = f"IF({start}<0,{LEN_TEXT}+{start}+1,{start}+1)"

        if end is None:
            p_end = f"{LEN_TEXT} + 1"
        elif isinstance(end, int):
            p_end = str(end + 1) if end >= 0 else f"{LEN_TEXT} {end + 1:+d}".replace("+0", "")
        else:
            p_end = f"IF({end}<0, {LEN_TEXT}+{end}+1,{end}+1)"

        if isinstance(start, int) and isinstance(end, int) and start >= 0 and end >= 0:
            length = str(max(0, end - start))
        elif start is None and isinstance(end, int) and end >= 0:
            length = str(end)
        else:
            length = f"MAX(0,{p_end}-({p_start}))"

        result = f"MID({value},{p_start},{length})"
        
        self.debug(result, 'result', 'getindex')

        self.level -= 1

        return result


    def raise_message(self, filename: str, message: str, keywords: str = None):
        try:
            if keywords is not None:
                # Keyword may be list, in that case
                if type(keywords) == str:
                    keywords = [keywords]


                # Find line
                lines = self.code.splitlines()

                lastFunc = ".;'\\."
                b = False
                for i in range(len(lines)):
                    for kw in keywords:
                        kw = str(kw)
                        if (kw in lines[i]) and (filename is None or filename == '?' or filename.lower().startswith(lastFunc.lower())):
                            ln = i + 1
                            line = lines[i].strip()
                            b = True                
                        
                    if lines[i].startswith("def "):
                        lastFunc = lines[i][4:].split('(')[0]
                    if b:
                        break
                else:
                    ln = '?'
                    line = '?'

                # If ?
                if filename == '?' or filename is None:
                    filename = lastFunc

                # Create nice ^^^
                ind = line.index(str(keywords[0]))
                locText = (' ' * ind) + ('^' * len(str(keywords[0])))

                msg = f"{message}\n  Detected to occur at line {ln} position {ind+1}:\n    {line}\n    {locText}"
            else:
                msg = message
        except Exception as e:
            msg = message

        return msg

    def raise_warning(self, message: str, keywords: str = None):
        """
        Adds a warning to the user but will not stop the code
        """

        ErrorMessage = self.raise_message('?', message, keywords)

        if self.ERROR_THRESHOLD <= 0:
            raise TypeError(ErrorMessage)
        else:
            self.warn(ErrorMessage)

    def get_int(self, expression: ast.Constant | ast.UnaryOp, allowNonInt: bool = False):
        """
        Get the integer value of an ast obj.
        If it is negative it uses UnaryOp so this fixes it.
        """
        if isinstance(expression, ast.UnaryOp) and isinstance(expression.op, ast.USub):
            return -expression.operand.value
        elif isinstance(expression, ast.UnaryOp) and isinstance(expression.op, ast.UAdd):
            return expression.operand.value
        elif not (isinstance(expression, ast.Constant) and isinstance(expression.value, int)) and not allowNonInt:
            self.raise_warning("Value must be a valid integer! Continuing anyway", ast.unparse(expression))
        return expression.value

    def get_value(self, expression: ast.Constant | ast.Name | ast.Call | ast.BinOp | str|int|float, noStrQuotes: bool = False) -> str:
        """Gets a value, which can be a cell, a standard value, etc"""
        self.level += 1
        self.debug(ast.dump(expression), 'expr', 'getval', expr=expression)
        result = self.get_straight_value(expression, noStrQuotes)
        self.debug(result, 'result', 'getval', expr=expression)
        self.level -= 1
        return result
    
    def get_straight_value(self, expression: ast.Constant | ast.Name | ast.Call | ast.BinOp | str|int|float, noStrQuotes: bool = False) -> str:
        """Gets a value, without any debug"""
        if isinstance(expression, (str, int, float)):
            return str(expression)
        elif isinstance(expression, bool):
            return str(expression).upper()

        if isinstance(expression, ast.Constant):
            if isinstance(expression.value, str):
                # Conv str > int > float
                if CONVERT_NUM_TO_STR:
                    try:
                        return str(int(expression.value))
                    except ValueError: 
                        try:
                            return str(float(expression.value))
                        except ValueError: 
                            pass

                if expression.value == '\n':
                    return "CHAR(10)"

                if '\n' in expression.value:
                    temp = []
                    for t in expression.value.split('\n'):
                        if t == '': 
                            temp.append("")
                        else:
                            temp.append('&"' + t.replace('"', '\\"') + '"')

                    return '&CHAR(10)'.join(temp).lstrip('&')

                if noStrQuotes:
                    return expression.value.replace('"', '\\"')
                
                return '"' + expression.value.replace('"', '\\"') + '"'
            else:
                return str(expression.value).upper()
        elif isinstance(expression, ast.UnaryOp):
            return str(self.get_int(expression))
        elif isinstance(expression, ast.JoinedStr):
            values = []
            for expr in expression.values:
                if isinstance(expr, ast.FormattedValue):
                    values.append(self.get_value(expr.value))
                else:
                    values.append(self.get_value(expr))
            return '&'.join(values)

        elif isinstance(expression, ast.Name):
            if expression.id.startswith('_') and expression.id in self.labels:
                return self.labels[expression.id]

            if expression.id in self.vars:
                return self.vars[expression.id]
            
            return expression.id
        elif isinstance(expression, ast.Call):
            return self.get_function(expression)
        elif isinstance(expression, ast.BinOp):
            if isinstance(expression.op, ast.FloorDiv):
                return f"FLOOR({self.get_value(expression.left)}/{self.get_value(expression.right)})"

            return self.get_value(expression.left) + convert_condition_astobj(expression.op) + self.get_value(expression.right)
        else:
            self.warn(f'Cannot parse value \'{ast.unparse(expression)}\'')
    
        return ''

    def ifexpr(self, expression: ast.If):
        """"""
        LN = f"IF"

        # Formula: IF(condition, truecode, falsecode)
        self.tempformula = self.currentFormula
        if isinstance(expression.test, ast.Compare):
            temp = 'IF('

            # Condition
            temp2 = [] 
            for i in range(len(expression.test.ops)):
                temp2.append( 
                    self.get_value(expression.test.left) + convert_condition_astobj(expression.test.ops[i]) + self.get_value(expression.test.comparators[i])
                )
            if len(temp2) == 1:
                temp += temp2[0]
            else:
                temp += 'AND(' + ','.join(temp2) + ')'

            # True code
            temp += ',' + (self.parse_list(expression.body, LN) or EMPTY)

            # False code
            temp += ',' + (self.parse_list(expression.orelse, LN) or EMPTY)

            return temp + ')'
        else:
            return f'IF({self.get_value(expression.test)},{self.parse_list(expression.body, LN) or EMPTY},{self.parse_list(expression.orelse, LN) or EMPTY})'
            
    def parse(self, expression: ast.stmt, levelName: str = "N/A"):
        self.level += 1
        self.debug(ast.dump(expression), 'expr', levelName, expr=expression)

        try:
            if isinstance(expression, ast.ImportFrom) and expression.module == 'syntax':
                pass

            # Value
            elif isinstance(expression, ast.Expr):
                return self.get_value(expression.value)

            elif isinstance(expression, ast.If):
                return self.ifexpr(expression)

            elif isinstance(expression, ast.Assign):
                for target in expression.targets:
                    self.vars[target.id] = self.get_value(expression.value)
                    self.debug(f"LABEL {target.id} = {self.get_value(expression.value)}", 'code', levelName, expr=expression)

            elif isinstance(expression, ast.Call):
                return self.get_function(expression)

            else:
                self.raise_warning(f"Expression '{ast.unparse(expression)}' skipped", ast.unparse(expression))

            return ''
        finally:
            self.level -= 1

    def get_function(self, expression: ast.Call) -> str:
        self.level += 1
        def get_arg(name: str|tuple[str], index: int, number: bool = False, noStrQuotes: bool = False, raw: bool = False, default: Any = None):
            if isinstance(name, str):
                name = (name, )

            for kw in expression.keywords:
                for n in name:
                    if kw.arg.lower() == n.lower():
                        if raw:
                            return kw.value
                        if number:
                            return self.get_int(kw.value)

                        return self.get_value(kw.value, noStrQuotes)
            if raw:
                return args[index]

            if number:
                return self.get_int(args[index])
            
            if default and index >= len(args):
                return default
            
            return self.get_value(args[index], noStrQuotes)
        try:
            self.debug(ast.dump(expression.func), 'expr', 'getfunc', expr=expression.func)
            if isinstance(expression.func, ast.Attribute):
                root = self.get_value(expression.func.value)
                name = expression.func.attr.lower()
                args = expression.args

                # Also put keywords in args
                for kw in expression.keywords:
                    args.append(kw.value)

                # "".replace()
                COMMON_ATTRS = {
                    'title': ('PROPER', ),
                    'lower': ('LOWER', ),
                    'casefold': ('LOWER', ),
                    'upper': ('UPPER', ),
                    'isprintable': ('ISTEXT', ),
                    'isnumeric': ('ISNUMBER', ),
                    'isdigit': ('ISNUMBER', ),
                    'isdecimal': ('ISNUMBER', ),
                }

                REGEX_CONVS = {
                    'isalpha': r'^[A-Za-z]+$',
                    'isalnum': r'^[A-Za-z0-9]+$',
                    'isspace': r'^\s+$',
                    'isascii': r'^[\x00-\x7F]*$',
                    # 'isdecimal': r'^\d+$',
                    # 'isnumeric': r'^\d+$',
                    # 'isdigit': r'^\d+$',
                    'islower': r'^[^A-Z]*[a-z][^A-Z]*$',
                    'isupper': r'^[^a-z]*[A-Z][^a-z]*$',
                    'istitle': r'^([^A-Za-z]*[A-Z][a-z]*)+[^A-Za-z]*$',
                }

                if name == 'casefold':
                    self.raise_warning("Casefold is automatically converted into lower. Unicode normalization is not supported", ast.unparse(expression.func.attr))

                if name in COMMON_ATTRS:
                    result = [root]
                    if len(COMMON_ATTRS[name]) > 1:
                        for i, a in enumerate(COMMON_ATTRS[name][1:]):
                            result.append(get_arg(a, i))
                    return COMMON_ATTRS[name][0] + '(' + ','.join(result) + ')'

                if name in REGEX_CONVS:
                    return f"IFERROR(REGEXMATCH({root},\"{REGEX_CONVS[name]}\"),FALSE)"

                match name:
                    ## String attributes
                    case 'replace':
                        # Python's replace 3rd arg is a max count, but in sheets, it is index based
                        # Thus an alternative is to keep repeating the substitude
                        def temp(c: int):
                            if c <= 1:
                                return f"SUBSTITUTE({root},{get_arg('old', 0)},{get_arg('new', 1)},1)"
                            
                            return f"SUBSTITUTE({temp(c-1)},{get_arg('old', 0)},{get_arg('new', 1)},1)"

                        if len(args) == 2 or (len(args) == 3 and get_arg('count', 2) == -1):
                            return f"SUBSTITUTE({root},{get_arg('old', 0)},{get_arg('new', 1)})"
                        elif len(args) == 3:
                            return temp(get_arg('count', 2, True))
                    case 'isprintable':
                        return f"ISTEXT({root}))"

                    case 'count':
                        if len(args) == 1:
                            return f"LEN({root})-LEN(SUBSTITUTE({root},{get_arg('sub', 0)},\"\"))"
                        elif 2 <= len(args) <= 3:
                            root = self.convert_indices(root, get_arg('start', 1), get_arg('end', 2))
                            return f"LEN({root})-LEN(SUBSTITUTE({root},{get_arg('sub', 0)},\"\"))"
                    case 'startswith' | 'endswith':
                        # Argument MAY be a tuple
                        result = []
                        if 1 <= len(args) <= 3:
                            prefix = get_arg('prefix', 0, raw=True)
                            if isinstance(prefix, (ast.Tuple, ast.List, ast.Set)):
                                prefixes = prefix.elts
                            else:
                                prefixes = (prefix, )
                            
                            if 2 <= len(args) <= 3:
                                root = self.convert_indices(root, get_arg('start', 1), get_arg('end', 2))

                            for p in prefixes:
                                if name == 'startswith':
                                    result.append(f"IFERROR(SEARCH({self.get_value(p)},{root})=1,FALSE)")
                                else:
                                    result.append(f"IFERROR(SEARCH({self.get_value(p)},{root})=LEN({root})-LEN({self.get_value(p)})+1,FALSE)")

                            if len(result) == 1:
                                return result[0]
                            else:
                                return "OR(" + ','.join(result) + ')'

                    case 'index' | 'find':
                        if 1 <= len(args) <= 3:
                            if 2 <= len(args) <= 3:
                                root = self.convert_indices(root, get_arg('start', 1), get_arg('end', 2))

                            result = f"SEARCH({get_arg('sub', 0)},{root})" + ('-1' if not RETURN_SHEET_INDEXES else '')

                            if name == 'find': # Find is the same thing, but -1 instead of error if not found
                                return f"IFERROR({result},-1)"
                            
                            return result
                    case 'center':
                        # Center formula: (width-len(str))//2 + str + ((width-len(str)) - (width-len(str))//2), width > len(str)

                        if 1 <= len(args) <= 2:
                            char = '" "' if len(args) == 1 else get_arg('fillchar', 1)
                            width = get_arg('width', 0)

                            return f"IF({width}<=LEN({root}),{root},REPT({char},FLOOR(({width}-LEN({root}))/2))&{root}&REPT({char},({width}-LEN({root})-FLOOR(({width}-LEN({root}))/2))))"

                    case _:
                        self.raise_warning(f"Attribute '{name}' is not recognized/supported", ast.unparse(expression))
                        return ''
      
                    
                self.raise_warning(f"Incorrect usage of attribute '{name}'", ast.unparse(expression))

            elif isinstance(expression.func, ast.Name):
                name = self.get_value(expression.func).upper()
                args = expression.args

                # Also put keywords in args
                for kw in expression.keywords:
                    args.append(kw.value)

                match name:
                    case 'CELL':
                        if len(args) == 1:
                            return get_arg('letter_OR_cell_as_str', 0).upper()
                        if len(args) == 2:
                            return get_arg('letter_OR_cell_as_str', 0).upper() + str(int(get_arg('index', 1, True))) # Use int() for type check
                    case 'CELLRANGE':
                        if len(args) == 2:
                            return get_arg('start', 0, noStrQuotes=True) + ':' + get_arg('end', 1, noStrQuotes=True)
                    case 'CELLREF':
                        if len(args) == 2:
                            return f"'{get_arg('sheet_name', 0, True).replace('"', '\\"')}'!{get_arg('cell', 1, noStrQuotes=True)}" 
                    case 'STR':
                        if len(args) == 1:
                            return get_arg(('text', 'string', 'object'), 0, True, True)

                    case _:
                        # Use compiled functions
                        values = []
                            
                        if name in FUNCTIONS:
                            # Get args:
                            if not FUNCTIONS[name]['$optcount'] <= len(args) <= FUNCTIONS[name]['$count']:
                                self.raise_warning(f"Incorrect (but using anyway) usage of function '{name}' (expected " + (f"between {FUNCTIONS[name]['$optcount']} to {FUNCTIONS[name]['$count']}" if FUNCTIONS[name]['$optcount'] != FUNCTIONS[name]['$count'] else str(FUNCTIONS[name]['$count'])) + f" arguments but got {len(args)})", ast.unparse(expression))
                                for i, arg in enumerate(args):
                                    values.append(get_arg(self.get_value(arg), i))
                            else:
                                # Check arg types
                                for i, arg in enumerate(FUNCTIONS[name]):
                                    if arg.startswith('$'): continue

                                    if i > len(args)-1: break

                                    userArg = get_arg(self.get_value(arg), i)
                                    values.append(userArg)

                                    if isinstance(FUNCTIONS[name][arg].annotation, ast.Name):
                                        argType = FUNCTIONS[name][arg].annotation.id
                                        if argType == 'Any': continue

                                        if '"' in userArg:
                                            if argType == 'int':
                                                self.raise_warning(f"Incorrect (but using anyway) usage of function '{name}' (expecting an integer, but got: {userArg})", ast.unparse(expression))
                                            elif argType in {'float', 'Time', 'Date', 'Cell', 'CellRange'}:
                                                self.raise_warning(f"Incorrect (but using anyway) usage of function '{name}' (expecting a {argType}, but got: {userArg} (which is a str))", ast.unparse(expression))

                                # Replace _ with ., and CELLINFO with CELL
                                if name == 'CELLINFO': name = 'CELL'
                                name = name.replace('_', '.')
                        else:
                            self.raise_warning(f"Function '{name}' is not recognized, using anyway", ast.unparse(expression))
                            for i, arg in enumerate(args):
                                values.append(get_arg(self.get_value(arg), i))
                            
                        return name + '(' + ','.join(values) + ')'

                        
                self.raise_warning(f"Incorrect usage of function '{name}'", ast.unparse(expression))
            return ''
        finally:
            self.level -= 1

    def print_warnings(self):
        if len(self.warnings) > 0:
            log.info("== WARNINGS ==")
            for i in range(len(self.warnings)):
                warning = self.warnings[i]

                log.warning(f"{i+1}. {warning}")

    def debug(self, msg: str, type: Literal['msg', 'code', 'expr', 'result'] = 'msg', levelName: str = "N/A", level: int = None, expr: ast.stmt = None):
        if level is None:
            level = self.level

        log.debug(f"{type}:L{level if level else self.level}:{levelName}: {msg if msg else '(empty)'}")
        self.debugLogs.append((time.process_time(), type, level, levelName, msg, expr))

    def print_debug(self, printGetVals: bool = False, maxLength: int = 300, codeFormat: bool = False, returnAsStr: bool = False):
        """Prints the debug log in a pretty format and returns the string"""
        result = []

        for time, type, level, levelName, msg, expr in self.debugLogs:
            temp = f"[{round(time, 3)}] "
            fmsg = msg[:maxLength-3] + '...' if len(msg) > maxLength else msg

            match type:
                case 'expr' | 'code':
                    # Ignore getval logs unless specified
                    if not printGetVals and levelName == 'getval': continue 

                    if codeFormat and type == 'expr':
                        t = []
                        for ln in ast.unparse(expr).splitlines():
                            c = (len(ln) - len(ln.lstrip(' '))) // 4
                            t.append(' ' * c + ln.lstrip(' '))
                        msg = '\\n'.join(t)

                    fmsg = msg[:maxLength-3] + '...' if len(msg) > maxLength else msg
                    
                    temp += (('  ' * (max(0, level-2)))) + ('↳ ' if level > 1 else '') + f"""{levelName}: {fmsg or '(empty)'}""" 
                case 'result':
                    temp += ('  ' * (level-1)) + '= ' + (fmsg or '(empty)')
                case 'msg':
                    temp += ('  ' * (level-1)) + f'{levelName}: ' + (fmsg or '(empty)')

            result.append(temp) if returnAsStr else print(temp)

        if returnAsStr:
            return result


    def parse_list(self, expressions: list[ast.stmt], levelName: str = "N/A"):
        results = []
        for i, t in enumerate(expressions, 1):
            LN = levelName+f'#{i}' if len(expressions) > 1 else levelName
            result = self.parse(t, LN)
            self.debug(result, 'result', LN, self.level+1)
            if result:
                results.append(result)
        if len(results) == 0:
            return ''
        elif len(results) > 1:
            if USE_FIRST_VALID:
                def temp(i):
                    if i >= len(results) - 1: return results[i]
                    expr = results[i]
                    return f"IF(OR({expr}=\"\",{expr}=FALSE),{temp(i+1)},{expr})" 
                self.raise_warning("There are multiple expressions in this code. The first non-empty and non-false will be used.", ast.unparse(expressions[0]))
                return temp(0)
            else:
                self.raise_warning("There are multiple expressions in this code. Only the last one will be chosen.", ast.unparse(expressions[0]))
        return results[-1]

        

    def build(self) -> str:
        """Starts the build process and returns the final output"""
        self.debug('Parsing code', 'msg', 'setup')
        parsed = ast.parse(self.code).body
        return '=' + (self.parse_list(parsed, 'root') or EMPTY)

        
        

        
if "__main__" in __name__:
    with open("code.py", 'r') as f:
        code = f.read()

    c = PyToSheetFormula(code)
    result = c.build()
    c.print_warnings()
    print(result)
