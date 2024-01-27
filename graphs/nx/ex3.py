import networkx as nx


def main():
    adjacency_matrix = []
    while True:
        try:
            line = input()
            if not line:
                break
            row = list(map(int, line.split()))
            adjacency_matrix.append(row)
        except EOFError:
            break

    G = nx.DiGraph()

    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                G.add_edge(i, j)

    distances = nx.shortest_path_length(G, source=0)

    for vertex in range(len(adjacency_matrix)):
        distance = distances.get(vertex, float('inf'))
        print(distance, end=" ")
    print()


main()
