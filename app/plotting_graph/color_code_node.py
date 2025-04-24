import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.cm as cm


def color_nodes_based_on_assignment(assignments, G, sources,pos,file_name,heating_demand):
    # Create a color map based on the assignments
    node_sizes = []
    node_colors = []
    labels = {}

    colormap = cm.get_cmap(
        "tab10", len(sources)
    )  # We can change 'tab10' to other colormaps

    source_to_color = {}
    for i, src_id in enumerate(sources):
        source_to_color[str(src_id)] = colormap(i)
    for node in G.nodes:

        node_data = G.nodes[node]

        # Size scale
        if node_data.get("type") == "Mixer":
            size = 1  # very small
            color = (1, 1, 1)
            labels[node] = f"{node}"  # format as needed

        elif node_data.get("type") == "Source":
            # color=(0,0,node*100)
            color = source_to_color.get(str(node), (0.5, 0.5, 0.5))
            size = 35  # very large
            labels[node] = f"{node}"  # format as needed

        else:
            '''
            5000- size 5
            '''
            labels[node] = f"{node} ={heating_demand[node]/1000}"  

            size = heating_demand.get(node, 0)/1000  # medium
            print(node, len(assignments[node]), assignments[node])
            if len(assignments[node]) == 0:
                color = (1,1,1)
            elif len(assignments[node]) > 1:
                color = (1, 0, 0)
            else:
                # color=(0,0,list(assignments[node].keys())[0]*100)
                source_id = list(assignments[node].keys())[0]
                color = source_to_color.get(str(source_id), (0.5, 0.5, 0.5))
        # node_sizes.append(size * 100)
        # print("\t",node_data.get("type"), size)

        node_sizes.append(size * 75)
        node_colors.append(color)
    
    # pos = nx.spring_layout(G)  # We can adjust the layout as needed
    nx.draw(
        G,
        pos,
        with_labels=True,
        font_weight="bold",
        node_size=node_sizes,
        node_color=node_colors,
        font_size=7,
        labels=labels
    )
    graph_name=f"network_plot_{file_name}.png"
    # Save the plot as an image file
    plt.savefig(
        graph_name
    )  # Save as PNG (you can change the file extension to PDF, SVG, etc.)
    plt.show()

    plt.close()
