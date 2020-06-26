# implementation of DFS in python
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited=set()
def dfs(visited,graph,node):
    if node not  in visited:
        print(node)
        visited.add(node)
        for neigh in graph[node]:
            dfs(visited,graph,neigh)

dfs(visited,graph,'A')