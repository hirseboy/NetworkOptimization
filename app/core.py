from app.minimization_problem.optimize_source import find_optimal_source
from app.plotting_graph.color_code_node import color_nodes_based_on_assignment
from app.plotting_graph.visualize_graph import visualize_heat_network
from app.reading_input.create_graph import create_graph_from_xml
def find_mass_flux(file_path, solver_name):
    G,sources,consumers = create_graph_from_xml(file_path)
    # print("Graph created",G.number_of_nodes(), G.number_of_edges())
    result=find_optimal_source(G,sources,consumers)
    print(result[-1])
    # visualize_heat_network(G,sources,consumers,result[-1])

    color_nodes_based_on_assignment(result[-1],G)