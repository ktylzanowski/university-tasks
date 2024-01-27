def if_association(edges):
    unique = set()

    for edge in edges:
        for vertex in edge:
            if vertex in unique:
                return "Nie jest to skojarzenie"
            unique.add(vertex)

    return "Jest to skojarzenie"


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

    tuple_list = []
    while True:
        try:
            row = input().strip()
            if not row:
                break
            first, second = map(int, row.split())
            tuple_list.append((first, second))
        except EOFError:
            break

    print(if_association(tuple_list))


if __name__ == "__main__":
    main()
