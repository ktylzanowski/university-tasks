class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i][2] < arr[left][2]:
        largest = left

    if right < n and arr[largest][2] < arr[right][2]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def minimum_spanning_tree(graph):
    n = len(graph)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != 0:
                edges.append((i + 1, j + 1, graph[i][j]))

    heap_sort(edges)
    disjoint_set = DisjointSet(n + 1)
    total_cost = 0

    for edge in edges:
        u, v, cost = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            total_cost += cost
            disjoint_set.union(u, v)

    return total_cost


def is_connected(graph):
    n = len(graph)
    disjoint_set = DisjointSet(n)

    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != 0 and disjoint_set.find(i) != disjoint_set.find(j):
                disjoint_set.union(i, j)

    root = disjoint_set.find(0)
    for i in range(1, n):
        if disjoint_set.find(i) != root:
            return False

    return True


def main():
    matrix = []
    while True:
        try:
            line = input()
        except EOFError:
            break

        if not line:
            break
        matrix.append([int(x) for x in line.split()])

    if not is_connected(matrix):
        print("Graf nie jest spójny")
    else:
        min_cost = minimum_spanning_tree(matrix)
        print(min_cost)



main()
