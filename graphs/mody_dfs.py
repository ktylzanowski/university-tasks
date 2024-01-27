def dfs(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    result_order = []

    while stack:
        current_vertex = stack[-1]

        if current_vertex not in visited:
            visited.add(current_vertex)
            result_order.append(current_vertex)

        unvisited_neighbors = [neighbor for neighbor in graph[current_vertex] if neighbor not in visited]

        if unvisited_neighbors:
            next_vertex = min(unvisited_neighbors)
            stack.append(next_vertex)
        else:
            stack.pop()

    return result_order


def is_connected(graph):
    start_vertex = next(iter(graph))
    visited = set()
    stack = [start_vertex]

    while stack:
        current_vertex = stack.pop()

        if current_vertex not in visited:
            visited.add(current_vertex)
            stack.extend(neighbor for neighbor in graph[current_vertex] if neighbor not in visited)

    return len(visited) == len(graph)


def main():
    adjacency_list = {}
    start_vertex = 1
    try:
        while True:
            line = input()
            if not line:
                break
            vertex, *neighbors = map(int, line.split())
            if vertex in adjacency_list:
                start_vertex = vertex
                break
            adjacency_list[vertex] = neighbors

        connected = is_connected(adjacency_list)
        if connected:
            result_order = dfs(adjacency_list, start_vertex)
            print("Porządek DFS:", " ".join(map(str, result_order)))
            print("Graf jest spójny")
        else:
            print("Graf jest niespójny")
    except EOFError:
        print("BŁĄD")


main()
