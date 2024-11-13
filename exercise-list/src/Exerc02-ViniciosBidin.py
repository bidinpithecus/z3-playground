# 2. Can you place all numbers from 1 to 16 into cells, such that the following 8 equations hold? Note that the operator “/” only works for non-remainder division, i.e. you can have 8/4 but not 8/3. As usual multiplication and division are performed before addition and subtraction.
# A + B / C = D
# +   -   -   +
# E / F + G = H
# *   *   /   /
# I + J + K = L
# =   =   =   =
# M - N / O = P
# From https://puzzling.stackexchange.com/questions/102658/4x4-grid-equations?noredirect=1

from z3 import *

if __name__ == "__main__":
  a, b, c, d = Ints('a b c d')
  e, f, g, h = Ints('e f g h')
  i, j, k, l = Ints('i j k l')
  m, n, o, p = Ints('m n o p')

  solver = SolverFor("QF_FD")

  cells = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
  solver.add(Distinct(cells))
  for cell in cells:
    solver.add(1 <= cell, cell <= 16)

  solver.add(b == c * (d - a))
  solver.add(e == f * (h - g))
  solver.add(l == i + (j + k))
  solver.add(n == o * (m - p))
  solver.add(m == a + (e * i))
  solver.add(n == b - (f * j))
  solver.add(g == k * (c - o))
  solver.add(h == l * (p - d))

  if solver.check() == sat:
    model = solver.model()
    solution = [[model[cell] for cell in row] for row in [[a, b, c, d], [e, f, g, h], [i, j, k, l], [m, n, o, p]]]
    print("sat:")
    for row in solution:
      print(row)
  else:
    print("unsat")
