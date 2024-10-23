from pulp import LpMaximize, LpProblem, LpStatus, LpVariable, lpSum

model = LpProblem(name="production_planning", sense=LpMaximize)

# Crude materials
u0 = LpVariable("u0", lowBound=0)
u1 = LpVariable("u1", lowBound=0)
u2 = LpVariable("u2", lowBound=0)


# End products
v0 = LpVariable("v0", lowBound=0)
v1 = LpVariable("v1", lowBound=0)

# End product segment amounts

v01 = LpVariable("v01", lowBound=0)
v02 = LpVariable("v02", lowBound=0)
v0T = LpVariable("v0T", lowBound=0)

v11 = LpVariable("v11", lowBound=0)
v12 = LpVariable("v12", lowBound=0)
v1T = LpVariable("v1T", lowBound=0)


# Revenue
z0 = LpVariable("z0", lowBound=0)
z1 = LpVariable("z1", lowBound=0)


# Objective function
model += lpSum([z0, z1, -3 * u0, -2 * u1, -u2])


# Constraints
model += (u0 + u1 + u2 <= 110, "capacity_in")
model += (v0 + v1 <= 90, "capacity_out")

model += (v0 == 0.7 * u0 + 0.4 * u1 + 0.3 * u2, "yield_crude1")
model += (v1 == 0.2 * u0 + 0.4 * u1 + 0.6 * u2, "yield_crude2")


model += (v0 == v01 + v02 + v0T, "sum of segments equals n of product 1")
model += (v01 <= 10, "units sold for product 1 segment 1")
model += (v02 <= 10, "units sold for product 1 segment 2")

model += (v1 == v11 + v12 + v1T, "sum of segments equals n of product 2")
model += (v11 <= 15, "units sold for product 2 segment 1")
model += (v12 <= 15, "units sold for product 2 segment 2")

model += (z0 == 4.0 * v01 + 3.5 * v02 + 3.0 * v0T, "product0 profit")
model += (z1 == 2.0 * v11 + 1.5 * v12 + 1.0 * v1T, "product1 profit")

# Solve
model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")

print(f"objective: {model.objective.value()}")


for var in model.variables():
    print(f"{var.name}: {var.value()}")


for name, c in model.constraints.items():
    print(f"{name} dual: {c.pi}, \t slack: {c.slack}")
