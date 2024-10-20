# Given a collection of integers, return the indices of any three elements which sum to zero. For instance, if you are given [−1, 6, 8, 9, 10, −100, 78, 0, 1], you could return {0, 7, 8} because −1+1+0 = 0. You can’t use the same index twice, and if there is no match you should return {−1, −1, −1}. From https://nathanleclaire.com/blog/2013/10/22/three-elements-that-sum-to-zero/

from z3 import *

def find_n_indices_with_m_sum(solver: Solver, arr: list[int], n: int, m: int) -> list[int]:
  indices = [-1 for _ in range(n)]
  len_array = len(arr)
  if n > len_array:
    return indices

  variables = [Int(f'i{i}') for i in range(n)]

  # Valid indices only
  for var in variables:
    solver.add(var >= 0, var < len_array)

  # Add constraints for valid index values
  solver.add(Distinct(variables))

  # Add a constraint for the sum of the selected array elements
  sum_expression = Sum([If(var == i, arr[i], 0) for var in variables for i in range(len_array)])
  solver.add(sum_expression == m)

  if solver.check() == sat:
    model = solver.model()
    return [model[var].as_long() for var in variables]
  else:
    return indices

if __name__ == "__main__":
  solver = Solver()

  arr = [-1, 6, 8, 9, 10, -100, 78, 0, 1]
  solution = find_n_indices_with_m_sum(solver, arr, 3, 0)

  print(solution)
