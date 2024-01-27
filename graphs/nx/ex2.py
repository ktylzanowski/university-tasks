import networkx as nx

file_path = 'lista.txt'
G = nx.read_adjlist(file_path, nodetype=int)

degree_2_nodes = [node for node, degree in G.degree() if degree == 2]

degree_2_nodes.sort()

print("Wierzchołki stopnia 2:", ' '.join(map(str, degree_2_nodes)))