
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    #1,2 1 => 2
    #1,3
    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

        #1 => [2,3]

    def printGraph(self):
        for node in self.graph:
            for v in self.graph[node]:
                print(node, "->", v)


g = Graph()

g.insertEdge(1, 2)
g.insertEdge(1, 100)
g.insertEdge(2, 3)
g.insertEdge(4, 5)

g.printGraph()