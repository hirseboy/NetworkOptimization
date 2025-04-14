import pulp
import numpy as np

# Example data
sources = ['S1', 'S2']
consumers = ['C1', 'C2', 'C3']

capacities = {'S1': 100, 'S2': 120}
heating_demand = {'C1': 50, 'C2': 60, 'C3': 40}

distance = {
    ('S1', 'C1'): 10,
    ('S1', 'C2'): 20,
    ('S1', 'C3'): 15,
    ('S2', 'C1'): 5,
    ('S2', 'C2'): 25,
    ('S2', 'C3'): 10,
}

penalty = {
    ('S1', 'C1'): 1,
    ('S1', 'C2'): 1.5,
    ('S1', 'C3'): 1,
    ('S2', 'C1'): 1,
    ('S2', 'C2'): 1,
    ('S2', 'C3'): 1.2,
}

# Create problem
prob = pulp.LpProblem("Minimize_Heat_Distribution_Cost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("assign", (sources, consumers), cat='Binary')

# Objective function
prob += pulp.lpSum(x[s][c] * distance[(s, c)] * heating_demand[c] * penalty[(s, c)] 
                   for s in sources for c in consumers)

# Constraints

# Each consumer gets assigned to exactly one source
for c in consumers:
    prob += pulp.lpSum(x[s][c] for s in sources) == 1

# Source capacity constraints
for s in sources:
    prob += pulp.lpSum(x[s][c] * heating_demand[c] for c in consumers) <= capacities[s]

# Solve
prob.solve()

# Results
for s in sources:
    for c in consumers:
        if x[s][c].varValue == 1:
            print(f"{c} is assigned to {s}")
