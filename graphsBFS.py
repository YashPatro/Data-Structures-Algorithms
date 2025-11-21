#21/11/25
a= [[] for i in range(5)]
print(a)
class Graph:
    def __init__(self,num):
        self.num = num
        self.adj = [[] for i in range(num)]
    def edges(self,x,y):
        self.adj[x].append(y)
        self.adj[y].append(x)
        print(self.adj)

graph1 = Graph(5)
graph1.edges(0,4)
graph1.edges(0,2)
graph1.edges(2,3)
graph1.edges(3,4)
graph1.edges(4,2)
graph1.edges(1,4)
