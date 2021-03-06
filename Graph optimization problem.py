"""
This is a sample Graph optimization problem with DFS and BFS methods
The result will be shown with a test graph section

DFS: Depth-First Search
BFS: Breadth-Fist search

@author: Manijeh Komeili
"""


class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, des):
        self.src = src
        self.des = des

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.des

    def __str__(self):
        return self.src.getName() + '->' + self.des.getName()


class WeightedEdge(Edge):
    def __init__(self, src, des, weight=1.0):
        self.src = src
        self.des = des
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.src.getName() + '-> (' + str(self.weight) + ')' + self.des.getName()


class Digraph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('This node is already exist')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        des = edge.getDestination()
        if not (src in self.nodes and des in self.nodes):
            raise ValueError('These nodes are not exist in our graph')
        self.edges[src].append(des)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        reverse = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, reverse)


def printPath(path):
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


def DFS(graph, start, end, path, shortest, printing=False):
    path = path + [start]
    if printing:
        print('current Depth-First search (DFS):', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newpath = DFS(graph, node, end, path, shortest, printing)
                if newpath != None:
                    shortest = newpath
    return shortest


def shortestPath(graph, start, end, printing=False):
    return DFS(graph, start, end, [], None, printing)


def BFS(graph, start, end, printing=False):
    initPath = [start]
    exploredPath = [initPath]
    if printing:
        print('current Breadth-Fist search (BFS):', printPath(exploredPath))
    while len(exploredPath) != 0:
        tmpPath = exploredPath.pop(0)
        print('current Breadth-Fist search (BFS):', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                exploredPath.append(newPath)
    return None


def testDFS_BFS():
    nodes = []
    for name in range(7):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[3], nodes[6]))
    g.addEdge(Edge(nodes[4], nodes[6]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[3], nodes[6]))
    g.addEdge(Edge(nodes[4], nodes[1]))

    spath_DFS = shortestPath(g, nodes[0], nodes[6], printing=True)
    print('The shortest path between start and end with DFS method: ', printPath(spath_DFS))
    spath_BFS = BFS(g, nodes[0], nodes[6])
    print('The shortest path between start and end with BFS method: ', printPath(spath_BFS))


testDFS_BFS()
