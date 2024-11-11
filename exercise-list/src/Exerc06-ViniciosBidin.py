# Harriet, upon returning from the mall, is happily describing her four shoe purchases to her friend Aurora. Aurora just loves the four different kinds of shoes that Harriet bought (ecru espadrilles, fuchsia flats, purple pumps, and suede sandals), but Harriet can’t recall at which different store (Foot Farm, Heels in a Handcart, The Shoe Palace, or Tootsies) she got each pair. Can you help these two figure out the order in which Harriet bought each pair of shoes, and where she bought each? • Harriet bought fuchsia flats at Heels in a Handcart. • The store she visited just after buying her purple pumps was not Tootsies. • The Foot Farm was Harriet’s second stop. • Two stops after leaving The Shoe Place, Harriet bought her suede sandals. Determine: Order - Shoes - Store

from z3 import *

shoes = ["cru espadrilles", "fuchsia flats", "purple pumps", "suede sandals"]
stores = ["Foot Farm", "Heels in a Handcart", "The Shoe Palace", "Tootsies"]

orders = {shoe: Int(f'pos_{shoe}') for shoe in shoes}
store_vars = {store: Int(f'pos_{store}') for store in stores}

solver = Solver()

solver.add([And(1 <= orders[shoe], orders[shoe] <= 4) for shoe in shoes])
solver.add(Distinct([orders[shoe] for shoe in shoes]))

solver.add([And(1 <= store_vars[store], store_vars[store] <= 4) for store in stores])
solver.add(Distinct([store_vars[store] for store in stores]))

solver.add(orders['fuchsia flats'] == store_vars["Heels in a Handcart"])

solver.add(orders['purple pumps'] + 1 != store_vars['Tootsies'])

solver.add(store_vars['Foot Farm'] == 2)

solver.add(store_vars['The Shoe Palace'] + 2 == orders['suede sandals'])

if solver.check() == sat:
    model = solver.model()
    solution = {shoe: model[orders[shoe]].as_long() for shoe in shoes}
    store_solution = {store: model[store_vars[store]].as_long() for store in stores}

    sorted_shoes = sorted(solution.items(), key=lambda x: x[1])
    sorted_stores = sorted(store_solution.items(), key=lambda x: x[1])

    print("Order - Shoes - Store")
    for i in range(4):
        shoe = sorted_shoes[i][0]
        store = sorted_stores[i][0].replace('_', ' ')
        print(f"{i + 1} - {shoe.capitalize()} - {store}")
else:
    print("No solution found.")