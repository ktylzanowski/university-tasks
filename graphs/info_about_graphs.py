def main():
    adjacency_list = get_adjacency_list()
    degrees = [len(neighbors) for neighbors in adjacency_list.values()]
    graph_info(adjacency_list, degrees)
    graph_classes = identify_graph_classes(degrees, adjacency_list)

    if graph_classes:
        print("\n".join(graph_classes))
    else:
        print("Graf nie należy do żadnej z podstawowych klas")


def get_adjacency_list():
    adjacency_list = {}

    try:
        while True:
            line = input()
            if not line:
                break
            vertex, *neighbors = map(int, line.split())
            adjacency_list[vertex] = neighbors
    except EOFError:
        pass

    return adjacency_list


def graph_info(adjacency_list, degrees):
    num_vertices = len(adjacency_list)

    degrees_str = ' '.join(map(str, degrees))

    num_edges = sum(degrees) // 2

    average_degree = sum(degrees) / num_vertices
    average_degree_str = str(int(average_degree)) if average_degree.is_integer() else average_degree
    print(f"Ilość wierzchołków: {num_vertices}")
    print(f"Ilość krawędzi: {num_edges}")
    print(f"Stopnie wierzchołków: {degrees_str}")
    print(f"Średni stopień: {average_degree_str}")


def identify_graph_classes(degrees, adj_list,):
    graph_classes = []

    if is_complete_graph(degrees):
        graph_classes.append("Jest to graf pełny")
    if is_cycle(degrees):
        graph_classes.append("Jest to cykl")
    if is_path(degrees):
        graph_classes.append("Jest to ścieżka")
    if is_tree(degrees) and is_connected(adj_list):
        graph_classes.append("Jest to drzewo")
    if is_hypercube(adj_list):
        graph_classes.append("Jest to hiperkostka")

    return graph_classes


def is_complete_graph(degrees):
    expected_degree = len(degrees) - 1
    return all(deg == expected_degree for deg in degrees)


def is_cycle(degrees):
    return all(deg == 2 for deg in degrees)


def is_path(degrees):
    return degrees.count(1) == 2 and degrees.count(2) == len(degrees) - 2


def is_tree(degrees):
    num_vertices = len(degrees)
    num_edges = sum(degrees) // 2
    return num_edges == num_vertices - 1


def is_connected(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    visited = set()
    start_node = list(graph.keys())[0]
    dfs(start_node)

    return len(visited) == len(graph)


def is_hypercube(graph):
    num_vertices = len(graph)
    n = 0
    while 2 ** n <= num_vertices:
        if 2 ** n == num_vertices:
            break
        n += 1
    else:
        return False

    for vertex in graph:
        if len(graph[vertex]) != n:
            return False

    num_dimensions = int(num_vertices.bit_length()) - 1
    for vertex in graph:
        binary_string = bin(vertex - 1)[2:].zfill(num_dimensions)
        for neighbor in graph[vertex]:
            neighbor_binary = bin(neighbor - 1)[2:].zfill(num_dimensions)
            diff_count = sum(bit1 != bit2 for bit1, bit2 in zip(binary_string, neighbor_binary))
            if diff_count not in [1, 2]:
                return False

    return True


main()