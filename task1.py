from pulp import LpProblem, LpMaximize, LpVariable, LpStatus

model = LpProblem(name="Beverage_Production", sense=LpMaximize)

x1 = LpVariable(name="Lemonade_units", lowBound=0, cat="Integer")
x2 = LpVariable(name="Fruit_juice_units", lowBound=0, cat="Integer")

model += x1 + x2, "Total_Products"

model += 2 * x1 + x2 <= 100, "Water_constraint"
model += x1 <= 50, "Sugar_constraint"
model += x1 <= 30, "Lemon_juice_constraint"
model += 2 * x2 <= 40, "Fruit_puree_constraint"

model += x1 <= 50, "Lemonade_production"
model += x2 <= 40, "Fruit_juice_production"


def main():

    model.solve()

    print(f"Status: {model.status}, {LpStatus[model.status]}")
    print(f"Lemonade units: {x1.varValue}")
    print(f"Fruit juice units: {x2.varValue}")
    print(f"Total Products: {model.objective.value()} units")

if __name__ == "__main__":
    main()