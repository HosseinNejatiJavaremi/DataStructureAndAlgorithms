class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):

        result = []

        indexOFSortList = 0
        indexOfResult = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while indexOfResult < self.V - 1:

            u, v, w = self.graph[indexOFSortList]
            indexOFSortList = indexOFSortList + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                indexOfResult = indexOfResult + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        for u, v, weight in result:
            print("{0} -- {1} == {2}".format(u, v, weight))


n = int(input("Enter number of vertices"))
g = Graph(n)
m = int(input("Enter number of edges"))
for i in range(m):
    edgeList = input("Enter u and v and weight of u-v").split(" ")
    g.addEdge(int(edgeList[0]), int(edgeList[1]), int(edgeList[2]))

g.kruskal()
