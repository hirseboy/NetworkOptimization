
# Installation 

`sudo apt install python3 python3-pip python3-venv`

## Creating Environment
`python3 -m venv venv`

`source venv/bin/activate`

## Running the code
`python3 app.py`

# Code

## Folder Structure

```
.
├── app
│   ├── heating_demand_edges
│   ├── minimization_problem
│   ├── plotting_graph
│   └── reading_input
├── data
│   └── test_scenarios
├── output
├── output_archive
└── tests

```

### reading_input
XML to Network Graph

The create_graph_from_xml() function parses a .vicus XML file to build a NetworkX graph representing a heating network. It performs the following steps:

1. Parses XML using xml.etree.ElementTree (or lxml, optionally).

2. Extracts Nodes:

        Nodes include attributes like id, type (e.g., Source, SubStation), and heating_demand.

        Consumers and sources are identified based on their type.

        Optional positional data is stored for visualization or layout.

3. Extracts Edges:

        Each edge connects two nodes with an optional length attribute used as the weight.

4. Returns:

        G: The constructed graph.

        source: List of source node IDs.

        consumer: List of consumer node IDs.

        pos: Dictionary of node positions (to construct the output graph)

### minimization_problem

The find_optimal_source() function solves a linear programming optimization problem to determine how to most efficiently distribute heat from sources to consumers across a network graph. It uses distance-weighted cost minimization while satisfying capacity and demand constraints.

1. Build Distance Matrix:

        Uses Dijkstra’s algorithm to calculate shortest path distances from each source to each consumer (weighted by edge 'length').
2. Formulate Optimization Problem (with PuLP):

- Decision Variables

        x[s][c]: fraction of consumer c’s demand supplied by source s.


- Objective Function:
            
        Minimize the total cost:
            
    $$
    \sum_{s, c} x[s][c] \cdot \text{demand}[c] \cdot (\text{distance}[s][c])^2
    $$

- Constraints:

        - Each consumer’s full demand must be met (sum of fractions = 1).
        - Each source cannot exceed its maximum capacity.