import matplotlib.pyplot as plt
import networkx as nx
import random

def visualize_heat_network(G,sources,consumers,assignments):

    pos = nx.spring_layout(G, weight='length', seed=42)

    # Node sizes by demand
    node_sizes = [G.nodes[n].get('heating_demand', 1) * 50 for n in G.nodes]

    # Random color for each source
    source_colors = {s: f"C{i}" for i, s in enumerate(sources)}

    node_colors = []
    for n in G.nodes:
        if n in sources:
            node_colors.append("black")
        elif n in consumers:
            assigned_source = assignments.get(n)
            node_colors.append(source_colors.get(assigned_source, "gray"))
        else:
            node_colors.append("lightgray")

    # Draw
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos,
            node_size=node_sizes,
            node_color=node_colors,
            with_labels=True,
            edge_color='gray',
            font_size=8)

    # Draw edge labels (lengths)
    edge_labels = {(u, v): f"{d['length']:.1f}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    # Legend
    for s, color in source_colors.items():
        plt.scatter([], [], c=color, label=f"Supplied by {s}")
    plt.scatter([], [], c="black", label="Source")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.title("Heat Network Assignment Visualization")
    plt.tight_layout()
    plt.show()