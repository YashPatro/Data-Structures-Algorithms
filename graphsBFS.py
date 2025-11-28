'''#21/11/25
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

#hw'''
class Graph:
    def __init__(self, num):
        self.num = num
        self.adj = [[] for _ in range(num)]

    def add_edge(self, x, y):
        self.adj[x].append(y)
        self.adj[y].append(x)  
    def show_adj_list(self):
        for i in range(self.num):
            print(f"{i}: {self.adj[i]}")


g = Graph(7)

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(4, 6)
g.add_edge(5, 6)

g.show_adj_list()
