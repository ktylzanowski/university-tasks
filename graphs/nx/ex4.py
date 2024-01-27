import networkx as nx
import numpy as np


def find_sources_and_sinks(graph):
    G = nx.DiGraph(graph)

    sources = [node for node, in_degree in G.in_degree() if in_degree == 0]
    sinks = [node for node, out_degree in G.out_degree() if out_degree == 0]

    return sources, sinks


def main():
    adjacency_matrix = []
    while True:
        try:
            row = input().split()
            if not row:
                break
            adjacency_matrix.append(list(map(int, row)))
        except EOFError:
            break

    adjacency_matrix_np = np.array(adjacency_matrix)

    sources, sinks = find_sources_and_sinks(adjacency_matrix_np)

    print(f"Ilość ujść: {len(sinks)}")
    print(f"Ilość źródeł: {len(sources)}")


main()




