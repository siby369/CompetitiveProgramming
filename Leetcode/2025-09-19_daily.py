"""
Problem: Spreadsheet Cell Operations (Custom Implementation)

Approach:
- Use a `defaultdict(int)` to store spreadsheet cells, which defaults missing cells to 0.
- Supported operations:
  - `setCell(cell, value)`: Set a cell (e.g., "A1") to the given integer value.
  - `resetCell(cell)`: Remove a cell from storage if it exists. (If the cell is not set, nothing changes.)
  - `getValue(formula)`: Evaluate a formula of the form "=X+Y":
    - Split the formula around the '+' sign.
    - Parse both left and right operands:
      - If it starts with an alphabet → treat it as a cell reference and fetch its value (default 0).
      - Otherwise → parse it directly as an integer.
    - Return the sum of the two operands.

Enhancement over previous version:
- Using `defaultdict(int)` eliminates the need for explicit `.get(..., 0)` checks, since missing cells automatically return 0.

Time Complexity:
- `setCell` / `resetCell`: O(1), dictionary operations.
- `getValue`: O(1), constant parsing and lookup.

Space Complexity: O(n), where n is the number of stored cells in the spreadsheet.
"""


class Spreadsheet:

    def __init__(self, rows: int):
        self.cells=defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell]=value

    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]
        else:
            return 0

    def getValue(self, formula: str) -> int:
        i=formula.index('+')
        l=formula[1:i]
        r=formula[i+1:]
        if l[0].isalpha():
            vl=self.cells[l]
        else:
            vl=int(l)
        if r[0].isalpha():
            vr=self.cells[r]
        else:
            vr=int(r)
        return vr+vl