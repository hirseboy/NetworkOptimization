
import networkx as nx
def assign_heating_demand_to_edges(G,assignments,heating_demand):
    for u, v in G.edges:
        G[u][v]['heat_flow'] = 0.0

    print(G.nodes(data=True))

    for consumer, source_info in assignments.items():
        for source, data in source_info.items():
            heat_amount = data['amount']

            try:
                # Find the shortest path from consumer to source
                path = nx.shortest_path(G, source=str(consumer), target=str(source))
                print(f"Path from {source} --> {consumer} -- {path}")
            except nx.NetworkXNoPath:
                print(f"No path from {consumer} to {source}")
                continue

            # Add the heat_amount to each edge in the path
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]

                if 'heat_flow' not in G[u][v]:
                    G[u][v]['heat_flow'] = 0.0
                G[u][v]['heat_flow'] += heat_amount
    print(G.edges(data=True))



