# 3. If 100 bushels of corn were distributed among 100 people in such a manner that each man received three bushels, each woman two, and each child half a bushel, how many men, women, and children were there? If we add the condition that there are five times as many women as men. That way, the solution becomes unique (otherwise, there are seven solutions). From: http://www.comp.nus.edu.sg/~henz/projects/puzzles/arith/index.html

# x + y + z = 100
# 3x + 2y + 0.5z = 100
# y = 5x

from z3 import *

if __name__ == "__main__":
  man, woman, child = Ints('man woman child')

  solver = Solver()

  types = [man, woman, child]
  for type in types:
    solver.add(0 <= type)

  solver.add(man + woman + child == 100)
  solver.add((3 * man) + (2 * woman) + (0.5 * child) == 100)
  solver.add(woman == 5 * man)

  if solver.check() == sat:
    model = solver.model()
    print("sat:")
    print(model)
  else:
    print("unsat")
