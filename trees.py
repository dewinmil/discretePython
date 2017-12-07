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

edgeGraph = {'A' : [['B', 10], ['D', 5]], 'B' : [['A', 10], ['C', 5]], 'C' : [['B', 5], ['D', 15]], 'D' : [['C', 15], ['A', 5]]}

def DFS(graph, node='A', visited=[]):
  visited.append(node)
  for n in graph[node]:
    dfs(graph, n, visited)
  return visited


def BFS(graph, node='A', visited=[], called=[]):
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



def edge_get(graph, node='A', visited=[], minimum = 999999999):
  oldMin = -1;
  newMin = 999999999;
  prevMin = minimum
  loop = True;

  while loop == True:
    for n in graph:
      for x in graph[n]:
        if (x[1] < newMin) and (x[1] > oldMin):
          minimum = x[1]
          newMin = x[1]
    oldMin = minimum
    newMin = 9999999
    if minimum == prevMin:
      loop = False

    if loop == True:
      for n in graph:
        for x in graph[n]:
          if x[1] == minimum:
            if [n, x[0]] and [x[0], n] not in visited:
              visited.append([n,x[0]])
    prevMin = minimum

  returnval = visited
  visited = []
  return returnval









   
