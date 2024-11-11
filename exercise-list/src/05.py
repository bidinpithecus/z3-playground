# Ten years from now Tim will be twice as old as Jane was when Mary was nine times as old as Tim. Eight years ago, Mary was half as old as Jane will be, when Jane is one year older than Tim will be at the time, when Mary will be five times as old as Tim will be two years from now. When Tim was one year old, Mary was three years older than Tim will be, when Jane is three times as old as Mary was six years before the time, when Jane was half as old as Tim will be, when Mary will be ten years older than Mary was, when Jane was one-third as old as Tim will be, when Mary will be three times as old as she was, when Jane was born. How old are the three persons now?

from z3 import *

T = Real('T')
J = Real('J')
M = Real('M')

t0 = Real('t0')
t1 = Real('t1')
t2 = Real('t2')
t3 = Real('t3')
t4 = Real('t4')
t5 = Real('t5')
t6 = Real('t6')
t7 = Real('t7')
t8 = Real('t8')

s = Solver()

s.add(T + 10 == 2 * (J - t0))
s.add(M - t0 == 9 * (T - t0))
s.add(M - 8 == (J + t1) / 2)
s.add(J + t1 == T + t2 + 1)
s.add(M + t2 == 5 * (T + 2))
s.add(T - t3 == 1)
s.add(M - t3 == T + 3 + t4)
s.add(J + t4 == 3 * (M - t5 - 6))
s.add(J - t5 == (T + t6) / 2)
s.add(M + t6 == M + 10 - t7)
s.add(J - t7 == (T + t8) / 3)
s.add(M + t8 == 3 * (M - J))

s.add(T >= 0, J >= 0, M >= 0)

if s.check() == sat:
    model = s.model()
    tim_age = model[T].as_long()
    jane_age = model[J].as_long()
    mary_age = model[M].as_long()
    print(f"Tim is {tim_age} years old, Jane is {jane_age} years old, and Mary is {mary_age} years old.")
else:
    print("No solution found.")
