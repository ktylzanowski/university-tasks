def graph_square(graph):
    squares = {}
    for u in graph:
        squares[u] = set(graph[u])
        for v in graph[u]:
            squares[u] |= set(graph[v]) - {u}

    result = []
    for u in sorted(squares):
        result_line = [u] + sorted(list(squares[u]))
        result.append(" ".join(map(str, result_line)))

    return result


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

    output = graph_square(adjacency_list)

    for line in output:
        print(line)


main()
