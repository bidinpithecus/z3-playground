# A bookstore offers a discount on your next purchase based on the amount spent today. If you buy a $20 book, you'll receive a 2% discount on your next purchase. Similarly, a $15 book grants a 1.5% discount next time, meaning that for every $10 spent, you get a 1% discount on your next purchase. 

from z3 import *

m = Real("m")
costs = [Real(f'cost{i + 1}') for i in range(5)]
discounts = [Real(f'discount{i + 1}') for i in range(5)]
prices = [10, 20, 30, 40, 50]

bought = [[Int(f'Book {i + 1}, Day {j + 1}') for j in range(5)] for i in range(5)]

solver = Optimize()

for i in range(5):
    solver.add(sum(bought[i]) == 1)
    solver.add(costs[i] == sum([prices[j] * bought[j][i] for j in range(5)]))
    if i == 0:
        solver.add(discounts[0] == 0)
    else:
        solver.add(discounts[i] == (costs[i - 1] / 1000) * costs[i])

    for j in range(5):
        solver.add(bought[i][j] >= 0)

for j in range(4):
    solver.add(Implies(sum([bought[i][j] for i in range(5)]) == 0, sum([bought[i][j + 1] for i in range(5)]) == 0))

solver.add(m == sum(prices) - sum(discounts))
h = solver.minimize(m)

if solver.check() == sat:
    model = solver.model()
    print("Optimal solution found:")
    print(f"Minimized total cost: ${model.eval(m)}")

    for i in range(5):
        for j in range(5):
            if model.eval(bought[i][j]) == 1:
                print(f"Book priced at ${prices[i]} was bought on day {j + 1}.")
        print(f"  Cost of book (after discount): ${model.eval(costs[i])}")
        print(f"  Discount applied on next purchase: {model.eval(discounts[i])}%")
else:
    print("No solution found.")
