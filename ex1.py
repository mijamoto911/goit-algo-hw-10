import pulp

model = pulp.LpProblem("maximize_production", pulp.LpMaximize)

lemonade = pulp.LpVariable("lemonade", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable("fruit_juice", lowBound=0, cat="Integer")

model += pulp.lpSum([lemonade, fruit_juice]), "Total_Products"

model += 2 * lemonade + fruit_juice <= 100, "water_constraint"
model += 1 * lemonade <= 50, "sugar_constraint"
model += 1 * lemonade <= 30, "lemon_juice_constraint"
model += 2 * fruit_juice <= 40, "fruit_puree_constraint"

model.solve()

print(f"Status: {model.status}, {pulp.LpStatus[model.status]}")
print(f"Total Lemonade produced: {lemonade.value()}")
print(f"Total Fruit Juice produced: {fruit_juice.value()}")
