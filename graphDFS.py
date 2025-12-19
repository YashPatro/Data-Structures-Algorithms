'''
class Graph:
    def __init__(self,nodes):
        self.nodes = nodes 
        self.adj = [[] for i in range(nodes)]
    def edges(self,x,y):
        self.adj[x].append(y)
        self.adj[y].append(x)
    def dfs(self,source, visited, response):
        response.append(source)
        visited[source] = True
        for i in self.adj[source]:
            if visited[i] == False:5
                self.dfs(i,visited, response)
    def traverval(self, source):
        visited = [False]*self.nodes
        response = []
        self.dfs(source, visited, response)
        
        return response
    
obj = Graph(5)
edges = int(input('enter numbet of edges you ant'))
for i in range(edges):
    x,y = map(int,list(input('enter adjecnent nodes').split()))
    obj.edges(x,y)

result = obj.traverval(1)
print(result)'''

#hw
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = [[] for i in range(nodes)]

    def edges(self, x, y):
        self.adj[x].append(y)
        self.adj[y].append(x)

    def dfs(self, source, destination, visited):
        if source == destination:
            return True

        visited[source] = True

        for i in self.adj[source]:
            if visited[i] == False:
                if self.dfs(i, destination, visited):
                    return True

        return False

    def path_exists(self, source, destination):
        visited = [False] * self.nodes
        return self.dfs(source, destination, visited)


#driver coee
obj = Graph(5)

edges = int(input('enter number of edges: '))
for i in range(edges):
    x, y = map(int, input('enter adjacent nodes: ').split())
    obj.edges(x, y)

start = int(input('enter start node: '))
end = int(input('enter end node: '))

if obj.path_exists(start, end):
    print('Path exists')
else:
    print('No path exists')
