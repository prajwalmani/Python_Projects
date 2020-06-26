# implementation od BFS algorithm in python
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
visited=[]
queue=[]

def bfs(visited,graph,source):
    visited.append(source)
    queue.append(source)

    while queue:
        s=queue.pop(0)
        print(s,end=' ')
        for node in graph[s]:
            if node not in visited:
                visited.append(node)
                queue.append(node)


bfs(visited,graph,'C')