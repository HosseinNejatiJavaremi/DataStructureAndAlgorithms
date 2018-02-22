from pythonds.graphs import Graph

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for Vertices in self:
            Vertices.setColor('white')
            Vertices.setPred(-1)
        for Vertices in self:
            if Vertices.getColor() == 'white':
                self.dfsvisit(Vertices)
                print("---------------------")

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        print(startVertex.id)
        self.time += 1
        startVertex.setFinish(self.time)

g = DFSGraph()

# g.addVertex(1)
# g.addVertex(2)
# g.addVertex(3)
# g.addVertex(4)
# g.addVertex(5)
# g.addVertex(6)
#
# g.addEdge(1,2)
# g.addEdge(2,3)
# g.addEdge(3,4)
# g.addEdge(1,3)
# g.addEdge(1,4)

n = int(input("Enter number of vertices"))
for i in range(n):
    g.addVertex(i)
m = int(input("Enter number of edges"))
for i in range(m):
    edgeList = input("Enter u and v").strip().split(" ")
    g.addEdge(int(edgeList[0]), int(edgeList[1]))

g.dfs()
