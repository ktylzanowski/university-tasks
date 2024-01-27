def LF_coloring(graph):
    def find_max_degree_colored():
        max_degree = -1
        max_degree_node = -1
        for node in range(1, len(graph) + 1):
            if not colored[node] and len(graph[node]) >= max_degree:
                max_degree = len(graph[node])
                max_degree_node = node
        return max_degree_node

    def find_min_color_neighbor(node):
        neighbors = graph[node]
        available_colors = set(range(1, len(graph) + 1))

        for neighbor in neighbors:
            if colored[neighbor] and color[neighbor] in available_colors:
                available_colors.remove(color[neighbor])

        return min(available_colors)

    num_nodes = len(graph)
    colored = [False] * (num_nodes + 1)
    color = [0] * (num_nodes + 1)

    while True:
        max_degree_node = find_max_degree_colored()

        if max_degree_node == -1:
            break

        colored[max_degree_node] = True
        color[max_degree_node] = find_min_color_neighbor(max_degree_node)
    coloring_result = [color[node] for node in range(1, num_nodes + 1)]
    chromatic_number = max(color)

    return coloring_result, chromatic_number


def main():
    adjacency_list = {}
    while True:
        try:
            row = input().strip()
            if not row:
                break
            vertex, *neighbors = map(int, row.split())
            adjacency_list[vertex] = neighbors
        except EOFError:
            break

    result, chromatic_number = LF_coloring(adjacency_list)

    print(f'Pokolorowanie wierzchołków: {" ".join(map(str, result))}')
    print(f'Liczba chromatyczna == {chromatic_number}')


main()