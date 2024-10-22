from pulp import LpMaximize, LpProblem, LpStatus, LpVariable, lpSum

model = LpProblem(name="production_planning", sense=LpMaximize)

# Crude materials
u0 = LpVariable("u0", lowBound=0)
u1 = LpVariable("u1", lowBound=0)
u2 = LpVariable("u2", lowBound=0)


# End products
v0 = LpVariable("v0", lowBound=0)
v1 = LpVariable("v1", lowBound=0)

# bjT units

b01 = LpVariable("b01", lowBound=0)
b02 = LpVariable("b02", lowBound=0)
b0T = LpVariable("b0T", lowBound=0)

b11 = LpVariable("b11", lowBound=0)
b12 = LpVariable("b12", lowBound=0)
b1T = LpVariable("b1T", lowBound=0)


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


model += (b01 <= 10, "units sold for product 1 segment 1")
model += (b02 <= 10, "units sold for product 1 segment 2")
model += (b0T == v0 - b01 - b02, "units sold for product 1 segment T")

model += (b11 <= 15, "units sold for product 2 segment 1")
model += (b12 <= 15, "units sold for product 2 segment 2")
model += (b1T == v1 - b11 - b12, "units sold for product 2 segment T")

model += (z0 == 4.0 * b01 + 3.5 * b02 + 3.0 * b0T, "product0 profit")
model += (z1 == 2.0 * b11 + 1.5 * b12 + 1.0 * b1T, "product1 profit")

# Solve
model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")

print(f"objective: {model.objective.value()}")


for var in model.variables():
    print(f"{var.name}: {var.value()}")


for name, c in model.constraints.items():
    print(f"{name} dual: {c.pi}, \t slack: {c.slack}")
