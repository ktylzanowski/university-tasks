def is_hamiltonian(graph, path, pos):
    if pos == len(graph):
        return True
    for v in range(len(graph)):
        if graph[path[pos - 1]][v] == 1 and v not in path:
            path[pos] = v
            if is_hamiltonian(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False


def is_hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0
    if not is_hamiltonian(graph, path, 1):
        return False
    is_True = graph[path[-1]][path[0]] == 1
    ##if is_True:
        ###print(path)
    return is_True


def is_hamiltonian_path(graph):
    path = [-1] * len(graph)
    path[0] = 0
    if not is_hamiltonian(graph, path, 1):
        return False
    is_True = not is_hamiltonian_cycle(graph)
    ##if is_True:
        ###print(path)
    return is_True


def is_connected(graph):
    visited = [False] * len(graph)
    dfs(graph, 0, visited)
    return all(visited)


def dfs(graph, vertex, visited):
    visited[vertex] = True
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and not visited[i]:
            dfs(graph, i, visited)


def main():
    graph = []
    while True:
        try:
            row = input().split()
            if not row:
                break
            graph.append(list(map(int, row)))
        except EOFError:
            break

    if not is_connected(graph):
        print("Graf jest niespójny")
    else:
        if is_hamiltonian_cycle(graph):
            print("Graf jest hamiltonowski")
        elif is_hamiltonian_path(graph):
            print("Graf jest półhamiltonowski")
        else:
            print("Graf nie jest hamiltonowski")


main()
