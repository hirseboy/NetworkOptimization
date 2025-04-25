import pulp
import networkx as nx

def find_optimal_source(G,sources,consumers):
    heating_demand = {c: G.nodes[c]['heating_demand'] for c in consumers}

    # Get source capacities from their heating_demand field
    capacities = {s: G.nodes[s]['heating_demand'] for s in sources}

    # print("Consumer demand: ",heating_demand)

    # print("Source capacity:",capacities)

    total_demand = sum(heating_demand.values())
    total_capacity = sum(capacities.values())
    print("Total Consumer demand:", total_demand, "\nTotal Source capacity:", total_capacity)

    # Build the distance matrix using shortest paths in the graph
    distance = {}
    for s in sources:
        lengths = nx.single_source_dijkstra_path_length(G, s, weight='length')
        for c in consumers:
            if c in lengths:
                distance[(s, c)] = lengths[c]
            else:
                print(f"No path from source {s} to consumer {c}")

    # Optimization model
    prob = pulp.LpProblem("Heat_Network_MinCostFlow", pulp.LpMinimize)

    # Decision variables: fraction of consumer demand supplied by source
    x = pulp.LpVariable.dicts("assign", (sources, consumers), lowBound=0, upBound=1, cat='Continuous')


    # Objective function: Minimize sum of demand * distance * fraction
    prob += pulp.lpSum(x[s][c] * heating_demand[c] * (distance[(s, c)] ** 2)
                       for s in sources for c in consumers if (s, c) in distance)

    # Each consumer must be fully satisfied

    for c in consumers:
        prob +=  pulp.lpSum(x[s][c] for s in sources if (s, c) in distance) == 1.00

    

    # Each source must not exceed its capacity
    for s in sources:
        prob +=  pulp.lpSum(x[s][c] * heating_demand[c] for c in consumers if (s, c) in distance) <= capacities[s]


    # Solve
    prob.solve()

    print("=========",x)

    # Results
    print("\nAssignments:")
    assignments={}
    for c in consumers:
        assignments[c]={}

    for s in sources:
        for c in consumers:
            if (s, c) in distance:
                val = x[s][c].varValue
                if val > 0:
                    print(f"{s} supplies {val * heating_demand[c]:.1f} to {c} ({val*100:.1f}%) consumer={heating_demand[c]}, source={capacities[s]}  distance= {distance[(s,c)]} ")

                    assignments[c][s]={
                        "fraction": round(val, 4),
                        "percentage": round(val * 100, 1),
                        "amount": round(val * heating_demand[c], 2)
                    }
    print("\nTotal cost:", pulp.value(prob.objective))

    print("Status:", pulp.LpStatus[prob.status])

    print(distance)
    return pulp.LpStatus[prob.status], heating_demand,assignments