import networkx as nx
import numpy as np


def read_adjacency_matrix():
    adjacency_matrix = []
    while True:
        try:
            row = input().split()
            if not row:
                break
            adjacency_matrix.append(list(map(int, row)))
        except EOFError:
            break
    return adjacency_matrix


def calculate_diameter(weighted_adjacency_matrix):
    G = nx.Graph(nx.from_numpy_array(np.array(weighted_adjacency_matrix)))

    all_pairs_shortest_paths = dict(nx.all_pairs_dijkstra_path_length(G))

    diameter = max(max(path_lengths.values()) for path_lengths in all_pairs_shortest_paths.values())
    return diameter


def main():
    matrix = read_adjacency_matrix()

    result = calculate_diameter(matrix)
    print(result)


main()