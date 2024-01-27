def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and (arr[i][0] < arr[l][0] or (arr[i][0] == arr[l][0] and arr[i][1] < arr[l][1])):
        largest = l
    if r < n and (arr[largest][0] < arr[r][0] or (arr[largest][0] == arr[r][0] and arr[largest][1] < arr[r][1])):
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def change_to_binary(nei):
    matrix = []
    for x in range(len(nei)):
        line = []
        for y in range(len(nei)):
            if y + 1 in nei[x] and y + 1 != nei[x][0]:
                line.append(1)
            else:
                line.append(0)
        matrix.append(line)
    return matrix


def is_directed(nei):
    matrix = change_to_binary(nei)
    for i in range(len(matrix) - 1):
        for j in range(len(matrix) - 1):
            if matrix[i][j] != matrix[j][i]:
                return 0
    return 1


def eqq(a):
    if a[0] > a[1]:
        return (a[1], a[0])
    else:
        return (a[0], a[1])


def is_edges(nei):
    graph_edges = []
    a = is_directed(nei)
    if a == 1:
        for i in range(len(nei)):
            for j in range(1, len(nei[i])):
                temp = []
                a = int(nei[i][j]) - 1
                b = (nei[i][0], nei[i][j])
                temp.append(b)
                p = nei[i][0]
                l = nei[i][j]
                temp2 = []
                for u in range(1, len(nei[i])):
                    b = (nei[i][0], nei[i][u])
                    if b[0] == p or b[1] == p or b[0] == l or b[1] == l:
                        if b not in temp and eqq(
                                b) not in temp and b not in temp2 and eqq(b) not in temp2:
                            b = eqq(b)
                            temp2.append(b)
                for w in range(1, len(nei[a])):
                    b = (nei[a][0], nei[a][w])
                    if b[0] == p or b[1] == p or b[0] == l or b[1] == l:
                        if b not in temp and eqq(
                                b) not in temp and b not in temp2 and eqq(b) not in temp2:
                            b = eqq(b)
                            temp2.append(b)
                heapSort(temp2)
                for y in temp2:
                    temp.append(y)
                z = 0
                for g in graph_edges:
                    if g[0] == temp[0] or g[0] == eqq(temp[0]):
                        z += 1
                if z == 0:
                    graph_edges.append(temp)
    elif a == 0:
        for i in range(len(nei)):
            for j in range(1, len(nei[i])):
                temp = []
                a = int(nei[i][j]) - 1
                b = (nei[i][0], nei[i][j])
                temp.append(b)
                for w in range(1, len(nei[a])):
                    b = (nei[a][0], nei[a][w])
                    if b not in temp:
                        temp.append(b)

                graph_edges.append(temp)
    return graph_edges


def print_graph_edges(graph_edges):
    for graf in graph_edges:
        for edge in graf:
            for ver in edge:
                print(ver, end="")
            print(" ", end="")
        print()


neig = []
edges = 0
while True:
    try:
        row = list(map(int, input().split()))
        neig.append(row)
    except EOFError:
        break
a = is_edges(neig)
for b in a:
    b = ' '.join(map(str, b))
    print(b)