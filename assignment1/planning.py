from pulp import LpMaximize, LpProblem, LpStatus, LpVariable, lpSum

# with open("small.dat", "r") as f:
#
#     content = f.readlines()
#     n_crudes = int(content[1].strip())
#     # print(f"Number of crudes: {n_crudes}")
#     crude_costs = [int(cost) for cost in content[3].strip().split(" ")]
#     # print(f"Crude costs {crude_costs}")
#     n_products = int(content[5].strip())
#     # print(f"Number of end products: {n_products}")
#     product_price = [int(price) for price in content[7].strip().split(" ")]
#     # print(f"Product market prices: {product_price}")
#     crude_yields = []
#     for index in range(9, 9 + n_crudes):
#         crude_yields.append([float(val) for val in content[index].strip().split(" ")])
#
#     # print(f"Crude yields: {crude_yields}")
#
#     capacity_input = int(content[13].strip())
#     # print(f"Capacity input: {capacity_input}")
#     capacity_output = int(content[15].strip())
#     # print(f"Capacity output: {capacity_output}")

model = LpProblem(name="production_planning", sense=LpMaximize)

# Crude materials
m0 = LpVariable("m0", lowBound=0)
m1 = LpVariable("m1", lowBound=0)
m2 = LpVariable("m2", lowBound=0)

# crudes = []

# End products
n0 = LpVariable("n0", lowBound=0)
n1 = LpVariable("n1", lowBound=0)


# Objective function
model += lpSum([4 * n0, 2 * n1, -3 * m0, -2 * m1, -m2])


# Constraints
model += (m0 + m1 + m2 <= 11, "capacity_in")
model += (n0 + n1 <= 9, "capacity_out")
model += (n0 == 0.7 * m0 + 0.4 * m1 + 0.3 * m2, "yield_crude1")
model += (n1 == 0.2 * m0 + 0.4 * m1 + 0.6 * m2, "yield_crude2")

# Solve
model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")

print(f"objective: {model.objective.value()}")


for var in model.variables():
    print(f"{var.name}: {var.value()}")


for name, c in model.constraints.items():
    print(f"{name} dual: {c.pi}, \t slack: {c.slack}")
