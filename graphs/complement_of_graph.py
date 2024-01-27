def complement(graph):
    vertices = set()
    for edge in graph:
        vertices.add(edge[0])
        vertices.update(edge[1:])

    complement_graph = {vertex: [] for vertex in vertices}

    for vertex in vertices:
        for other_vertex in vertices:
            if vertex != other_vertex and other_vertex not in graph[vertex - 1]:
                complement_graph[vertex].append(other_vertex)

    return complement_graph


def print_adjacency_list(graph):
    for vertex, neighbors in graph.items():
        if neighbors:
            string = f"{vertex} {' '.join(map(str, neighbors))}"
        else:
            string = vertex
        print(string)


def parse_input():
    graph = []
    while True:
        try:
            line = input().strip()
            if not line:
                break

            values = list(map(int, line.split()))
            graph.append(values)
        except EOFError:
            break
    return graph


g = parse_input()

complement_result = complement(g)

print_adjacency_list(complement_result)
