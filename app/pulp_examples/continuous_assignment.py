import pulp

# Define sources and consumers
sources = ['S1', 'S2']
consumers = ['C1', 'C2', 'C3']

# Define source capacities and consumer heating demands
capacities = {'S1': 100, 'S2': 120}
heating_demand = {'C1': 50, 'C2': 60, 'C3': 40}

# Distance matrix
distance = {
    ('S1', 'C1'): 10,
    ('S1', 'C2'): 20,
    ('S1', 'C3'): 15,
    ('S2', 'C1'): 5,
    ('S2', 'C2'): 25,
    ('S2', 'C3'): 10,
}

# Create LP problem
prob = pulp.LpProblem("Minimize_Total_Heat_Cost", pulp.LpMinimize)

# Decision variables: fraction of each consumer's demand fulfilled by each source
x = pulp.LpVariable.dicts("assign", (sources, consumers), lowBound=0, upBound=1, cat='Continuous')

# Objective: Minimize total cost = demand * distance * fraction
prob += pulp.lpSum(x[s][c] * heating_demand[c] * distance[(s, c)] for s in sources for c in consumers)

# Constraint: each consumer's demand must be fully satisfied
for c in consumers:
    prob += pulp.lpSum(x[s][c] for s in sources) == 1

# Constraint: source capacity must not be exceeded
for s in sources:
    prob += pulp.lpSum(x[s][c] * heating_demand[c] for c in consumers) <= capacities[s]

# Solve
prob.solve()

# Results
print("\nAssignment Fractions:")
for s in sources:
    for c in consumers:
        assigned = x[s][c].varValue
        if assigned > 0:
            supplied_amount = assigned * heating_demand[c]
            print(f"{s} supplies {supplied_amount:.2f} to {c} ({assigned*100:.1f}%)")

# Total cost
print("\nTotal Cost:", pulp.value(prob.objective))
