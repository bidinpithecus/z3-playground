from z3 import *

def getCells(nQueens: int) -> list[list[Bool]]:
    return [[Bool(f'q{i}{j}') for j in range(nQueens)] for i in range(nQueens)]

def getRows(cells: list[list[Bool]]) -> list[list[Bool]]:
    return [row for row in cells]

def getCols(cells: list[list[Bool]]) -> list[list[Bool]]:
    nQueens = len(cells)
    return [[cells[i][j] for i in range(nQueens)] for j in range(nQueens)]

def getDiagonals(cells: list[list[Bool]]) -> list[list[Bool]]:
    n = len(cells)
    main_diagonals = [[cells[i][j] for i in range(n) for j in range(n) if i - j == k] for k in range(-n + 2, n - 1)]
    anti_diagonals = [[cells[i][j] for i in range(n) for j in range(n) if i + j == k] for k in range(1, 2 * n - 2)]
    return main_diagonals + anti_diagonals

# Each row must have at least one queen
def addAtLeastOneQueenPerRow(solver: Solver, cells: list[list[Bool]]) -> Solver:
    rows = getRows(cells)
    solver.add([Or(row) for row in rows])
    return solver

# Each row must have at most one queen
def addAtMostOneQueenPerRow(solver: Solver, cells: list[list[Bool]]) -> Solver:
    rows = getRows(cells)
    solver.add([AtMost(*row, 1) for row in rows])
    return solver

# Each column must have at most one queen
def addAtMostOneQueenPerCol(solver: Solver, cells: list[list[Bool]]) -> Solver:
    cols = getCols(cells)
    solver.add([AtMost(*col, 1) for col in cols])
    return solver

# Each diagonal must have at most one queen
def addAtMostOneQueenPerDiagonal(solver: Solver, cells: list[list[Bool]]) -> Solver:
    diagonals = getDiagonals(cells)
    solver.add([AtMost(*diag, 1) for diag in diagonals if len(diag) > 1])
    return solver

if __name__ == "__main__":
    if len(sys.argv) != 2:
      print(f"Usage: {sys.argv[0]} <number of queens>")
      exit(-1)

    nQueens: int = int(sys.argv[1])
    cells = getCells(nQueens)

    solver = Solver()

    # Adding constraints
    solver = addAtLeastOneQueenPerRow(solver, cells)
    solver = addAtMostOneQueenPerRow(solver, cells)
    solver = addAtMostOneQueenPerCol(solver, cells)
    solver = addAtMostOneQueenPerDiagonal(solver, cells)

    if solver.check() == sat:
        model = solver.model()
        print("sat")
        for i in range(nQueens):
            row = ""
            for j in range(nQueens):
                row += "Q " if model[cells[i][j]] else "· "
            print(row)
    else:
        print("unsat")
