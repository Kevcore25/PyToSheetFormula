from typing import *
from functions import *
from vars import *

UppercaseCharacter = Literal['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

true = True
false = False


# Built-in functions. Pre-built functions can be found in functions.py
def CELL(letter_OR_cell_as_str: UppercaseCharacter | str[Cell | CellRange], index: Optional[int]) -> Cell:
    """
    A cell value.
    You can also directly do something like, `A1`; however, this is mainly used for including `$`.

    This function also supports cell ranges, like `CELL('$A4:$A5')`
    """
    # Although it has no effect, this shows what it really does
    if index:
        return str(letter_OR_cell_as_str)+str(int(index))
    else:
        return str(letter_OR_cell_as_str)
cell = CELL


def CELLRANGE(start: Cell | CellRange, end: Cell | CellRange) -> CellRange | Range:
    """
    A cell range value.
    You can also directly do something like, `A1|A2` or `A|B`
    """
    return str(start)+':'+str(end) # Although it has no effect, this shows what it really does
cellrange = CELLRANGE

def CELLREF(sheet_name: str, cell: Cell | CellRange | str[Cell | CellRange]) -> Cell | CellRange:
    """
    A cell value, from a different tab name.

    """
    # Although it has no effect, this shows what it really does
    return f"'{sheet_name.replace("'", "\\'")}'!{cell}"
cellref = CELLREF

def STR(text: str) -> str:
    """
    A set text value without any quotations.
    """