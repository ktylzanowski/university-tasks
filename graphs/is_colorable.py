def is_colorable(adjacency_list, colors):
    num_vertices = len(adjacency_list)

    for vertex in range(1, num_vertices + 1):
        for neighbor in adjacency_list[vertex]:
            if colors[vertex - 1] == colors[neighbor - 1]:
                return False

    return True


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

    colors = list(map(int, input().split()))

    if is_colorable(adjacency_list, colors):
        print("Graf jest kolorowalny")
    else:
        print("Graf nie jest kolorowalny")


main()