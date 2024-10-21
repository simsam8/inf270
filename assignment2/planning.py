from pulp import LpMaximize, LpProblem, LpStatus, LpVariable, lpSum

model = LpProblem(name="production_planning", sense=LpMaximize)

# Crude materials
u0 = LpVariable("u0", lowBound=0)
u1 = LpVariable("u1", lowBound=0)
u2 = LpVariable("u2", lowBound=0)

# crudes = []

# End products
v0 = LpVariable("v0", lowBound=0)
v1 = LpVariable("v1", lowBound=0)

# bjT units

b0T = LpVariable("b0T", lowBound=0)
b1T = LpVariable("b1T", lowBound=0)


z0 = LpVariable("z0", lowBound=0)
z1 = LpVariable("z1", lowBound=0)


# Objective function
model += lpSum([z0, z1, -3 * u0, -2 * u1, -u2])


# Constraints
model += (u0 + u1 + u2 <= 110, "capacity_in")
model += (v0 + v1 <= 90, "capacity_out")
model += (v0 == 0.7 * u0 + 0.4 * u1 + 0.3 * u2, "yield_crude1")
model += (v1 == 0.2 * u0 + 0.4 * u1 + 0.6 * u2, "yield_crude2")

model += (10 + 10 + b0T == v0, "v0 sold")
model += (15 + 15 + b1T == v1, "v1 sold")

model += (z0 == 4.0 * 10 + 3.5 * 10 + 3.0 * b0T, "product0 profit")
model += (z1 == 2.0 * 15 + 1.5 * 15 + 1.0 * b1T, "product1 profit")

# Solve
model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")

print(f"objective: {model.objective.value()}")


for var in model.variables():
    print(f"{var.name}: {var.value()}")


for name, c in model.constraints.items():
    print(f"{name} dual: {c.pi}, \t slack: {c.slack}")
