import xml.etree.ElementTree as ET
# from lxml import etree as ET
import networkx as nx
import os
from pathlib import Path

def create_graph_from_xml():

    # data_file_path = Path(__file__).resolve().parents[2] / 'data' / 'example_with_namepsace.xml'
    data_file_path = Path(__file__).resolve().parents[2] / 'data' / 'testcase01.vicus'
    # data_file_path = Path(__file__).resolve().parents[2] / 'data' / 'trail.vicus'
    print(data_file_path)
    if not os.path.exists(data_file_path):
        print("No File exists")
        return
    
    # Load and parse the XML
    try:
        tree = ET.parse(data_file_path)
        # root = tree.getroot()
        # root = ET.fromstring(data_file_path.read_text())
        
        # tree = ET()
        # root=tree.parse(data_file_path)
        # Proceed with processing the XML data
    except ET.ParseError as e:
        print(f"Parse error: {e}")
        return
    
    print(root.tag)
    return
    