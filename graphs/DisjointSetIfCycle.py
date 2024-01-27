class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def has_cycle(graph):
    n = len(graph)
    ds = DisjointSet(n)

    for i in range(n):
        for j in range(i, n):
            if graph[i][j] == 1:
                root_i = ds.find(i)
                root_j = ds.find(j)

                if root_i == root_j:
                    return True
                else:
                    ds.union(root_i, root_j)

    return False


def main():
    matrix = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            break
        row = [int(x) for x in line.split()]
        matrix.append(row)

    if has_cycle(matrix):
        print("TAK")
    else:
        print("NIE")

main()