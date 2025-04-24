from app.heating_demand_edges.assign_heating_demand_to_edges import assign_heating_demand_to_edges
from app.minimization_problem.optimize_source import find_optimal_source
from app.plotting_graph.color_code_node import color_nodes_based_on_assignment
from app.reading_input.create_graph import create_graph_from_xml

def find_mass_flux(file_path, solver_name):
    G,sources,consumers,pos = create_graph_from_xml(file_path)
    # print("Graph created",G.number_of_nodes(), G.number_of_edges())
    result,heating_demand,assignments=find_optimal_source(G,sources,consumers)
    print(assignments)

    assign_heating_demand_to_edges(G,assignments,heating_demand)
    return
    # visualize_heat_network(G,sources,consumers,result[-1])
    graph_name=str(file_path).split("/")[-1].replace(".vicus", "")
    print(graph_name)

    color_nodes_based_on_assignment(assignments,G,sources,pos,graph_name,heating_demand)