def dijkstra(graph, start):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        min_distance = float('inf')
        min_index = -1

        for i in range(num_vertices):
            if distances[i] < min_distance and not visited[i]:
                min_distance = distances[i]
                min_index = i

        visited[min_index] = True

        for i in range(num_vertices):
            if not visited[i] and graph[min_index][i] > 0:
                new_distance = distances[min_index] + graph[min_index][i]
                if new_distance < distances[i]:
                    distances[i] = new_distance

    return distances


def diameter(graph):
    num_vertices = len(graph)
    max_diameter = 0

    for i in range(num_vertices):
        distances = dijkstra(graph, i)
        max_distance = max(distances)
        max_diameter = max(max_diameter, max_distance)

    return max_diameter


def periphery(graph):
    num_vertices = len(graph)
    periphery_vertices = []

    graph_diameter = diameter(graph)

    for i in range(num_vertices):
        distances = dijkstra(graph, i)
        max_distance = max(distances)

        if max_distance == graph_diameter:
            periphery_vertices.append(i + 1)

    return sorted(periphery_vertices)


def getMatrix():
    matrix = []
    while True:
        try:
            line = input()
        except EOFError:
            break

        if not line:
            break
        matrix.append([int(x) for x in line.split()])
    return matrix


def main():
    input_matrix = getMatrix()

    result = periphery(input_matrix)
    result_str = ' '.join(map(str, result))
    print(result_str)


main()
