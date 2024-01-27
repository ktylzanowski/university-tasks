import networkx as nx
from ast import literal_eval

graph_dict_str = input()
graph_dict = literal_eval(graph_dict_str)
graph = nx.Graph(graph_dict)
complement_graph = nx.complement(graph)
complement_adj_matrix = nx.adjacency_matrix(complement_graph).todense()

print(complement_adj_matrix)

line_graph = nx.line_graph(graph)
line_adj_matrix = nx.adjacency_matrix(line_graph).todense()

print(line_adj_matrix)
