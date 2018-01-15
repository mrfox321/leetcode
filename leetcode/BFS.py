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


def BFS(graph):

    start = graph[0]
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

edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
n = 6
graph = constructGraph(n,edges)
end = BFS(graph)
print end.dist
