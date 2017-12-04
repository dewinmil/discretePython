graph = {
    'A' : ['B','C'],
    'B' : [],
    'C' : ['D','E'],
    'D' : [ 'F'],
    'E' : ['G'],
    'F' : ['H'],
    'G' : [],
    'H' : [],
}

dfsGraph = {'A' : ['B', 'C'], 'B' : ['D'], 'C' : [], 'D' : [],}
bfsGraph = {'A' : ['B', 'C', 'D'], 'B' : [], 'C' : [], 'D' : [],}


def dfs(graph, node, visited):
  visited.append(node)
  for n in graph[node]:
    dfs(graph, n, visited)
  return visited

def bfs(graph, node, visited, called):
  if node not in visited:
    visited.append(node)
  if node not in called:
    called.append(node)
  for n in graph[node]:
    visited.append(n)
  for x in visited:
    if x not in called:
      bfs(graph, x, visited, called)
  return visited

visited = dfs(dfsGraph,'A', [])
print ("dfs of {'A' : ['B', 'C'], 'B' : ['D'], 'C' : [], 'D' : [],}")
print(visited)

visited = bfs(bfsGraph, 'A', [], [])
print("")
print("bfs of {'A' : ['B', 'C', 'D'], 'B' : [], 'C' : [], 'D' : [],}")
print(visited)

   
