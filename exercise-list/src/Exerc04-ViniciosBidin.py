# If you start with my age, in years, and apply the four operations: +2; /8; −3; ∗7 in some order, then the final answer you get is my husband’s age in years. Funnily enough, if you start with his age and apply the same four operations in a different order, then you get my age. What are our two ages? From: https://enigmaticcode.wordpress.com/2015/06/20/enigma-1224-age-changing/

from z3 import *


m = Int('m')
h = Int('h')

age_constraints = And(m > 13, h > 13)

perm1 = [Int(f'perm1_{i}') for i in range(4)]
perm2 = [Int(f'perm2_{i}') for i in range(4)]

hlist = [Real(f'hlist_{i}') for i in range(5)]
mlist = [Real(f'mlist_{i}') for i in range(5)]

operations = [
    lambda x: x + 2,
    lambda x: x / 8,
    lambda x: x - 3,
    lambda x: x * 7 
]

solver = Solver()

solver.add(Distinct(perm1), Distinct(perm2))
solver.add([And(1 <= perm1[i], perm1[i] <= 4) for i in range(4)])
solver.add([And(1 <= perm2[i], perm2[i] <= 4) for i in range(4)])

solver.add(hlist[0] == m)
solver.add(mlist[0] == h)

for i in range(4):
    solver.add(
        hlist[i + 1] == If(perm1[i] == 1, operations[0](hlist[i]),
                           If(perm1[i] == 2, operations[1](hlist[i]),
                              If(perm1[i] == 3, operations[2](hlist[i]),
                                 operations[3](hlist[i]))))
    )
    solver.add(
        mlist[i + 1] == If(perm2[i] == 1, operations[0](mlist[i]),
                           If(perm2[i] == 2, operations[1](mlist[i]),
                              If(perm2[i] == 3, operations[2](mlist[i]),
                                 operations[3](mlist[i]))))
    )

solver.add(hlist[4] == h)
solver.add(mlist[4] == m)

solver.add(age_constraints)

if solver.check() == sat:
    model = solver.model()
    my_age_val = model[m].as_long()
    husband_age_val = model[h].as_long()
    print(f"My age: {my_age_val}")
    print(f"Husband's age: {husband_age_val}")
else:
    print("No solution found.")
