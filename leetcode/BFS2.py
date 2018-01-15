class Graph():

    def __init__(self,num):

        self.vertex = {}

        for i in xrange(num):
            self.vertex[i] = Vertex(i)


    def addEdges(self,edges):
        for i in xrange(len(self.vertex)):
            for edge in edges:
                if self.vertex[i].name in edge:
                    for node in edge:
                        if node != self.vertex[i].name:
                            self.vertex[i].adj.append()

    class Vertex():

        def __init__(self,name):
            self.index = name
            self.adj = []
            self.color = 0
            self.dist = float('inf')
            self.parent = None
            
