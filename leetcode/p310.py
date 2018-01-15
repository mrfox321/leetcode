import collections

class vertices():

    def __init__(self,name,edges):

        self.adj = []
        self.vertex = name
        self.color = 0
        self.dist = float("inf")
        self.parent = None
        self.addEdges(edges)

    def addEdges(self,edges):
        for edge in edges:
            if self.vertex in edge:
                for node in edge:
                    if node != self.vertex:
                        self.adj.append(node)

def constructGraph(n,edges):
    graph = {}

    for i in xrange(n):
        graph[i] = vertices(i,edges)

    return graph


def BFS(start,graph):

    start.dist = 0
    queue = collections.deque()
    queue.appendleft(start)

    while queue:
        u = queue.pop()
        for v_point in u.adj:
            v = graph[v_point]
            if v.color == 0:
                v.color = 1
                v.dist = u.dist + 1
                v.parent = u
                queue.appendleft(v)
        u.color = 2

        if not queue:
            return u

def returnNode(end,distance):

    steps = distance//2
    print distance
    for i in xrange(steps):
        end = end.parent
    node = []
    node.append(end.vertex)
    if distance%2 == 0:
        return node
    else:
        node.append(end.parent.vertex)
        return node


def minHeight(n,edges):
    graph = constructGraph(n,edges)
    end1 = BFS(graph[0],graph)
    print end1.dist,end1.vertex
    graph = constructGraph(n,edges)
    end2 = BFS(end1,graph)
    print end2.dist,end2.vertex

    distance = end2.dist

    return returnNode(end2,distance)

edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
n = 6
print minHeight(n,edges)
