from app.reading_input.create_graph import create_graph_from_xml


def find_mass_flux():
    graph = create_graph_from_xml()
    print("Graph created",graph.number_of_nodes(), graph.number_of_edges())
    
    