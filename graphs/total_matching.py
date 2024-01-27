from itertools import combinations

class GraphMatching:
    def __init__(self, V):
        self.V = V
        self.adjList = [[] for _ in range(V)]
        self.visited = [False] * V
        self.match = [-1] * V

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def dfs(self, u):
        self.visited[u] = True
        for v in self.adjList[u]:
            w = self.match[v]
            if w == -1 or (not self.visited[w] and self.dfs(w)):
                self.match[v] = u
                return True
        return False

    def isCompleteMatching(self):
        for i in range(self.V):
            self.match[i] = -1

        matchCount = 0
        for i in range(self.V // 2):
            for j in range(self.V):
                self.visited[j] = False
            if self.dfs(i):
                matchCount += 1
        if matchCount == self.V // 2 and self.checkAdditionalConditions():
            return True
        return False

    def checkAdditionalConditions(self):
        for k in range(1, self.V + 1):
            for combination in combinations(range(self.V), k):
                neighbors_set = set()
                for vertex in combination:
                    neighbors_set.update(self.adjList[vertex])

                if len(neighbors_set) == k * 2:
                    return True

        return False

    def displayMatching(self):
        print("Skojarzenie całkowite:")
        for i in range(self.V // 2, self.V):
            print(f"Wierzchołek {self.match[i] + 1} skojarzony z wierzchołkiem {i}")


def scan():
    lines = []
    while True:
        try:
            line = input()
            if not line:
                break
            lines.append(line)

        except EOFError:
            break

    V = len(lines)
    g = GraphMatching(V)

    for i in range(V):
        s = lines[i].split(" ")
        createEdges(s, g)

    return g


def createEdges(arr, g):
    for i in range(1, len(arr)):
        g.addEdge(int(arr[0]) - 1, int(arr[i]) - 1)


if __name__ == "__main__":
    g = scan()

    if g.isCompleteMatching():
        print("Istnieje skojarzenie doskonałe")
        ### g.displayMatching()
    else:
        print("Nie istnieje skojarzenie doskonałe")
