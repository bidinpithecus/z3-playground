# Each weekday, Bonnie takes care of five of the neighbors’ children. The children’s names are Keith, Libby, Margo, Nora, and Otto; last names are Fell, Gant, Hall, Ivey, and Jule. Each is a different number of years old, from two to six. Can you find each child’s full name and age? • One child is named Libby Jule. • Keith is one year older than the Ivey child, who is one year older than Nora. • The Fell child is three years older than Margo. • Otto is twice as many years old as the Hall child. Determine: First name - Last name - Age

from z3 import *

first_names = ["Keith", "Libby", "Margo", "Nora", "Otto"]
last_names = ["Fell", "Gant", "Hall", "Ivey", "Jule"]
ages = [2, 3, 4, 5, 6]

var_first_names = {first_name: Int(f'pos_{first_name}') for first_name in first_names}
var_last_names = {last_name: Int(f'pos_{last_name}') for last_name in last_names}
var_ages = {age: Int(f'age_{age}') for age in ages}

solver = Solver()

solver.add([And(1 <= var_first_names[first_name], var_first_names[first_name] <= 5) for first_name in first_names])
solver.add(Distinct([var_first_names[first_name] for first_name in first_names]))

solver.add([And(1 <= var_last_names[last_name], var_last_names[last_name] <= 5) for last_name in last_names])
solver.add(Distinct([var_last_names[last_name] for last_name in last_names]))

solver.add([And(1 <= var_ages[age], var_ages[age] <= 5) for age in ages])
solver.add(Distinct([var_ages[age] for age in ages]))

solver.add(var_first_names["Libby"] == var_last_names["Jule"])

solver.add(var_ages[5] == var_first_names["Keith"]) 
solver.add(var_ages[4] == var_last_names["Ivey"])   
solver.add(var_ages[3] == var_first_names["Nora"])  

solver.add(var_last_names["Fell"] == var_first_names["Margo"] + 3)

solver.add(var_first_names["Otto"] == var_last_names["Hall"] * 2)

if solver.check() == sat:
    model = solver.model()
  
    solution = {first_name: model[var_first_names[first_name]].as_long() for first_name in first_names}
    last_name_solution = {last_name: model[var_last_names[last_name]].as_long() for last_name in last_names}
    age_solution = {age: model[var_ages[age]].as_long() for age in ages}

  
    sorted_first_names = sorted(solution.items(), key=lambda x: x[1])
    sorted_last_names = sorted(last_name_solution.items(), key=lambda x: x[1])
    sorted_ages = sorted(age_solution.items(), key=lambda x: x[1])

  
    print("First Name - Last Name - Age")
    for i in range(5):
        first_name = sorted_first_names[i][0]
        last_name = sorted_last_names[i][0]
        age = sorted_ages[i][0]
        print(f"{first_name} - {last_name} - {age} years old")
else:
    print("No solution found.")
