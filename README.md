# PyToSheetFormula
A program that translates Python expressions into a spreadsheet formula.
Designed for Google Sheets.

## How to use:
1. Clone this repository
2. Add your expression in code.py (for example, `if A1 == "Hello": "World"`)
3. Run the `compiler.py` file

## Notes:
- It supports most Google Sheet functions, which you can find in `functions.py`
- It should support most Python string methods, such as `.startswith()`, `.count()`, and `.find()`
- There is no print or return function. Just simply write the expression down (e.g. `A1.count(" ")`) in your code
