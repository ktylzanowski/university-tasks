import networkx as nx
import numpy as np


def is_hamiltonian(graph):
    return nx.is_connected(graph) and all(nx.degree(graph, node) >= graph.number_of_nodes() // 2 for node in graph.nodes)


def is_semi_hamiltonian(graph):
    return nx.is_connected(graph) and any(nx.degree(graph, node) == graph.number_of_nodes() // 2 for node in graph.nodes)


def is_hamiltonian_path(graph):
    return nx.is_connected(graph) and nx.is_eulerian(graph)


def main():
    input_matrix = []
    while True:
        try:
            line = input().strip()
            if not line:
                break
            row = list(map(int, line.split()))
            input_matrix.append(row)
        except EOFError:
            break

    adjacency_matrix = np.array(input_matrix)
    graph = nx.Graph(adjacency_matrix)

    if not nx.is_connected(graph):
        print("Graf jest niespójny")
    else:
        if is_hamiltonian(graph):
            print("Graf jest hamiltonowski")
        elif is_semi_hamiltonian(graph):
            print("Graf jest półhamiltonowski")
        else:
            print("Graf nie jest hamiltonowski")


main()