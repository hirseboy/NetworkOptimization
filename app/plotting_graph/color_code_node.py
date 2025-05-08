import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from pathlib import Path

def color_nodes_based_on_assignment(assignments, G, sources,pos,file_name,heating_demand):
    # Create a color map based on the assignments
    node_sizes = []
    node_colors = []
    # labels = {}

    colormap = cm.get_cmap(
        "tab10", len(sources)
    ) 

    source_to_color = {}
    for i, src_id in enumerate(sources):
        source_to_color[str(src_id)] = colormap(i)


    for node in G.nodes:
        node_data = G.nodes[node]

        # Size scale
        if node_data.get("type") == "Mixer":
            size = 1  # very small
            color = (1, 1, 1)
            # labels[node] = f"{node}"  # format as needed

        elif node_data.get("type") == "Source":
            # color=(0,0,node*100)
            color = source_to_color.get(str(node), (0.5, 0.5, 0.5))
            size = 30  # very large
            # labels[node] = f"{node}"  # format as needed

        else:
            '''
            5000- size 5
            '''

            size = heating_demand.get(node, 0)/1000  # medium
            print(node, len(assignments[node]), assignments[node])
            if len(assignments[node]) == 0:
                color = (1,1,1)
            elif len(assignments[node]) > 1:
                color = (1, 0, 0)
            else:
                source_id = list(assignments[node].keys())[0]
                color = source_to_color.get(str(source_id), (0.5, 0.5, 0.5))

        node_sizes.append(size * 75)
        node_colors.append(color)

    # ----- Handle edge widths and colors -----
    heat_flows = [data.get("heat_flow", 0) for _, _, data in G.edges(data=True)]
    if heat_flows:
        norm = mcolors.Normalize(vmin=min(heat_flows), vmax=max(heat_flows))
        edge_cmap = cm.get_cmap("plasma")  # or 'hot', 'viridis', etc.

        edge_colors = [edge_cmap(norm(data.get("heat_flow", 0))) for _, _, data in G.edges(data=True)]
        edge_widths = [max(0.5, data.get("heat_flow", 0) / 5000.0) for _, _, data in G.edges(data=True)]
    else:
        edge_colors = "gray"
        edge_widths = 1

    fig, ax = plt.subplots()  # Step 1: Create figure and ax
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes,ax=ax)
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=edge_widths,ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=8,ax=ax, font_family="serif",font_weight="bold")
    ax.autoscale() 
    sm = plt.cm.ScalarMappable(cmap=edge_cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax,shrink=0.8)
    cbar.set_label("Heat Flow (W)", fontsize=12)


    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)

    graph_name=output_dir/ f"network_plot_{file_name}.png"
    plt.title(f"Network Graph: {file_name}", fontsize=14)
    plt.axis("off")
    plt.tight_layout()

    # Save the plot as an image file
    plt.savefig(
        graph_name
    )  
    plt.show()

    plt.close()
