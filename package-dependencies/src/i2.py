from z3 import *

# Packages
a, b, c, d, e, f, g, z = Bools('a b c d e f g z')

s = Solver()

# Dependencies
s.add(Implies(a,And(b, c, z)))
s.add(Implies(b, d))
s.add(Implies(c, And(Or(d, e), Or(f, g))))

# Conflicts
s.add(Not(And(d, e)))
s.add(Not(And(d, g)))

# Required packages
s.add(And(a, z))

asw = s.check()
if asw == sat:
    m = s.model()
    print(m)
else: 
    print('unsat')
