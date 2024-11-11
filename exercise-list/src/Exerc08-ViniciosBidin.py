# You have five bales of hay. For some reason, instead of being weighed individually, they were weighed in all possible combinations of two. The weights of each of these combinations were written down and arranged in numerical order, without keeping track of which weight matched which pair of bales. The weights, in kilograms, were 80, 82, 83, 84, 85, 86, 87, 88, 90, and 91. How much does each bale weigh? Is there a solution? Are there multiple possible solutions? From: https://mathlesstraveled.com/2009/12/16/the-haybaler/

from z3 import *

bales = [Int(f'bale_{i}') for i in range(5)]

solver = Solver()

solver.add([bale > 0 for bale in bales])

pairwise_weights = [80, 82, 83, 84, 85, 86, 87, 88, 90, 91]

solver.add(bales[0] + bales[1] == pairwise_weights[0])
solver.add(bales[0] + bales[2] == pairwise_weights[1])

solver.add(bales[3] + bales[4] == pairwise_weights[len(pairwise_weights) - 1])
solver.add(bales[2] + bales[4] == pairwise_weights[len(pairwise_weights) - 2])

solver.add(sum(bales) == sum(pairwise_weights) / 4)

if solver.check() == sat:
    model = solver.model()
    bale_weights = [model[bale].as_long() for bale in bales]
    bale_weights.sort()
    print(f"The weights of the five bales are: {bale_weights}")
else:
    print("No solution found.")
