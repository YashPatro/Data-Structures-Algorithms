class Graph:
    def __init__(self, num):
        self.num = num
        self.adj = [[] for _ in range(num)]

    def add_edge(self, x, y):
        self.adj[x].append(y)
        self.adj[y].append(x)
    def BFS_trav(self,start):
        visited = [False]*self.num
        result  = []
        queue = []
        queue.append(start)
        visited[start] = True
        while len(queue) > 0:
            ValA = queue.pop(0)
            result.append(ValA)
            for i in self.adj[ValA]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return result

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

print(g.BFS_trav(0))
print(g.BFS_trav(1))

g.show_adj_list()
