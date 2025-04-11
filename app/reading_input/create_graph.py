import xml.etree.ElementTree as ET
# from lxml import etree as ET
import networkx as nx
import os
from pathlib import Path

def create_graph_from_xml():

    data_file_path = Path(__file__).resolve().parents[2] / 'data' / 'testcase01.vicus'
    print(data_file_path)

    if not os.path.exists(data_file_path):
        print("No File exists")
        return
    
    # Load and parse the XML
    try:
        tree = ET.parse(data_file_path)
        root = tree.getroot()
        
    except ET.ParseError as e:
        print(f"Parse error: {e}")
        return
    
    print(root.tag)
     # === 1. Extract Nodes ===
    ns = {'IBK': 'http://www.ibk-software.de/IBK'}
    G = nx.Graph()

    for node in root.findall(".//NetworkNode"):
        node_id = node.get("id")
        node_type = node.get("type")
        heating_demand = 0

        param = node.find(".//IBK:Parameter", namespaces=ns)
        # param = node.find(".//IBK:Parameter[@name='MaxHeatingDemand']", namespaces=ns)
        if param is not None:
            heating_demand = float(param.text)

        # Add node with attributes
        G.add_node(node_id, type=node_type, heating_demand=heating_demand)
        print("Node: ", node_id)
        print("Type: ",node_type)
        print("Heating Demand :", heating_demand)

    # === 2. Extract Edges ===
    for edge in root.findall(".//NetworkEdge"):
        node1 = edge.get("idNode1")
        node2 = edge.get("idNode2")
        length_elem = edge.find("Length")
        length = float(length_elem.text) if length_elem is not None else 0

        # Add edge with weight/length
        G.add_edge(node1, node2, length=length)

    # === 3. Print Summary ===
    print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")

    print()
    # Print example node and edge
    for node in list(G.nodes(data=True))[:5]:
        print("Node:", node)

    print()
    for edge in list(G.edges(data=True))[:5]:
        print("Edge:", edge)

    return
    