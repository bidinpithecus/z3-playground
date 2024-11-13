# In three dollars, you get 5 bananas, in five dollars, 7 oranges, in seven dollars, 9 mangoes and in nine dollars, three apples, I need to purchase 100 fruits in 100 dollars. Please keep in mind that all type of fruits need to be purchased but I do not like banana and apple, so these should be of minimum quantity.

from z3 import *

apples, bananas, mangoes, oranges = Ints('apples bananas mangoes oranges')

solver = Optimize()

solver.add(apples > 0, bananas > 0, mangoes > 0, oranges > 0)

solver.add(bananas + oranges + mangoes + apples == 100)
solver.add((3.0 / 5) * bananas + (5.0 / 7) * oranges + (7.0 / 9) * mangoes + 3 * apples <= 100)

solver.minimize(bananas)
solver.minimize(apples)

# solver.add(bananas <= mangoes, bananas <= oranges)
# solver.add(apples <= mangoes, apples <= oranges)

if solver.check() == sat:
    model = solver.model()
    apple_count = model[apples].as_long()
    banana_count = model[bananas].as_long()
    mango_count = model[mangoes].as_long()
    orange_count = model[oranges].as_long()
    
    apple_cost = (apple_count / 3) * 9
    banana_cost = (banana_count / 5) * 3
    mango_cost = (mango_count / 9) * 7
    orange_cost = (orange_count / 7) * 5

    print(f"Apples: {apple_count}, Cost: ${apple_cost:.2f}")
    print(f"Bananas: {banana_count}, Cost: ${banana_cost:.2f}")
    print(f"Mangoes: {mango_count}, Cost: ${mango_cost:.2f}")
    print(f"Oranges: {orange_count}, Cost: ${orange_cost:.2f}")
else:
    print("No solution found.")