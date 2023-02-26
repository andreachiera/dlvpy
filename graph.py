import matplotlib.pyplot as plt
import networkx as nx
from dlvpy.program.program import Program
from dlvpy.program.options import Options

def draw_graph(edge_color_blue = {}, edge_color_red = {}, filename = "graph.png"):
    G = nx.Graph()

    if edge_color_blue is not None:
        for edge in edge_color_blue:
            G.add_edges_from([(edge_color_blue[edge]["from"], edge_color_blue[edge]["to"], {'weight': edge_color_blue[edge]["weight"], 'color': 'b'})])

    if edge_color_red is not None:
        for edge in edge_color_red:
            G.add_edges_from([(edge_color_red[edge]["from"], edge_color_red[edge]["to"], {'weight': edge_color_red[edge]["weight"], 'color': 'r'})])

    pos = nx.spring_layout(G, k=10)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    colors = nx.get_edge_attributes(G, 'color').values()
    nx.draw_networkx_edges(G, pos, edge_color=colors)
    all_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_labels(G, pos, font_family="sans-serif", font_color="w")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=all_labels)
    plt.box(False)
    plt.savefig(filename)

dlv_path = "C:\\dlvpy\\bin\\windows\\dlv.mingw.exe"

p = Program()
options: Options = Options(dlv_path)
options.add_options(["-n=1", "-pfilter=path,arc", "-N=1000000"])

p.add_logic_rules("""
    number_node(3).
    number_arcs(4).
    node(X) :- number_node(Z), #int(1, Z, X).
    arc(X, Y, W) :- node(X), node(Y), X!=Y, #int(2, 5, W).
    graph(X, Y, W) v out_graph(X, Y, W) :- arc(X, Y, W).
    path(X, Y) :- graph(X, Y, _).
    path(X, Z) :- path(X, Y), graph(Y, Z, _).
    %:- graph(X,Y1,_), graph(X,Y2,_), graph(X,Y3,_), graph(X,Y4,_)
    %:- #count{ X, Y : graph(X, Y, _)} > K, number_arcs(K).
    %:- #count{ X, Y : graph(X, Y, _)} < K, number_arcs(K).
    %:- node(X), node(Y), X!=Y, not path(X, Y).
    %:- node(X), #count{ X: graph(X, _, _) } > 2.
    % schema(graph(key(autoincrement), "from", "to", "weight"))
""")

p.execute(options)
last_result = p.get_last_result(False)
print(last_result)
answer_set_schema_results = last_result[0]["model"]["schema_results"]
(graph, config) = answer_set_schema_results[0]
draw_graph(graph)



