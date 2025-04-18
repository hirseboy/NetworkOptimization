import matplotlib.pyplot as plt
import networkx as nx
def color_nodes_based_on_assignment(assignments, G):
    # Create a color map based on the assignments
    node_sizes = []
    node_colors = []
    print("d" ,G.nodes(data=True))
    for node in G.nodes:
        # if node in assignments:
        #     color = 'green'  # Nodes with assignments will be green (i.e., consumers or sources involved in the assignment)
        # else:
        #     color = 'red'    # Nodes not involved in any assignment can be red (optional)
        # node_colors.append(color)
        
        node_data = G.nodes[node]

        # Size scale
        if node_data.get("type") == "mixer":
            size = 100  # very small
        elif node_data.get("type")  == "Source":
            size = 10000  # very large
        else:
            size = 500  # medium
        node_sizes.append(size * 100)
    # Draw the graph
    pos = nx.spring_layout(G)  # You can adjust the layout as needed
    nx.draw(G, pos, with_labels=True, node_color=node_colors, font_weight='bold', node_size=node_sizes)
    plt.show()
    # Save the plot as an image file
    plt.savefig('network_plot.png')  # Save as PNG (you can change the file extension to PDF, SVG, etc.)
    plt.close()

