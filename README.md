# PyToSheetFormula
A program that translates Python expressions into a spreadsheet formula.
Designed for Google Sheets.

## How to use:
1. Clone this repository
2. Add your expression in code.py (for example, `if A1 == "Hello": "World"`)
3. Run the `compiler.py` file

## Decompiling (formula to Python):
1. Paste a formula (for example, `=IF(A1="Hello","World","")`) into `formula.txt`
2. Run the `decompiler.py` file, which prints Python code that `compiler.py` can compile back
3. Parts with no Python equivalent (such as `{1,2;3,4}` arrays or `#N/A`) are kept as raw text with `STR()`

## Notes:
- It supports most Google Sheet functions, which you can find in `functions.py`
- It should support most Python string methods, such as `.startswith()`, `.count()`, and `.find()`
- There is no print or return function. Just simply write the expression down (e.g. `A1.count(" ")`) in your code
