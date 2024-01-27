import networkx as nx


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


def find_minimum_spanning_tree_weight(adjacency_matrix):
    G = nx.Graph()
    for i in range(len(adjacency_matrix)):
        for j in range(i + 1, len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] != 0:
                G.add_edge(i, j, weight=adjacency_matrix[i][j])

    if not nx.is_connected(G):
        print("Graf nie jest spójny")
        return False
    minimum_spanning_tree = nx.minimum_spanning_tree(G)
    weight = sum(edge[2]['weight'] for edge in minimum_spanning_tree.edges(data=True))

    return weight


def main():
    adjacency_matrix = read_adjacency_matrix()
    weight = find_minimum_spanning_tree_weight(adjacency_matrix)
    if weight:
        print(weight)


main()
