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



def min_kruskal(graph, node='A', visited=[], minimum = 999999999):
  visited = edge_get(graph, node, visited, minimum)
  connectedPoint =[]
  connectedTree = []
  connectedTreePoint = []
  nonConnectedTree = []

  connectedPoint.append(visited[0][0])
  connectedPoint.append(visited[0][1])
  connectedTreePoint.append(visited[0][0])
  connectedTreePoint.append(visited[0][1])
  connectedTree.append(visited[0])

  for n in visited:
    for c in nonConnectedTree:
      if c[0] in connectedTreePoint or c[1] in connectedTreePoint:
        connectedTree.append(c)
        if c[0] not in connectedTreePoint:
          connectedTreePoint.append(c[0])
        if c[1] not in connectedTreePoint:
          connectedTreePoint.append(c[1])
        nonConnectedtree.remove(c)

    if n[0] not in connectedPoint or n[1] not in connectedPoint:
      if n[0] in connectedTreePoint:
        connectedTree.append(n)
        connectedPoint.append(n[1])
        connectedTreePoint.append(n[1])
      elif n[1] in connectedTreePoint and n[0] not in connectedTreePoint:
        connectedTree.append(n)
        connectedTreePoint.append(n[0])
        if n[0] not in connectedPoint:
          connectedPoint.append(n[0])
      else:
        nonConnectedTree.append(n)
        if n[0] not in connectedPoint:
          connectedPoint.append(n[0]) 
        if n[1] not in connectedPoint:
          connectedPoint.append(n[1])
  
  loop = True
  while loop:
    for n in visited:
      for c in nonConnectedTree:
        if c[0] in connectedTreePoint or c[1] in connectedTreePoint:
          connectedTree.append(c)
          if c[0] not in connectedTreePoint:
            connectedTreePoint.append(c[0])
          if c[1] not in connectedTreePoint:
            connectedTreePoint.append(c[1])
          nonConnectedTree.remove(c)
      
      if n[0] in connectedTreePoint and n[1] not in connectedTreePoint:
        connectedTree.append(n)
        connectedTreePoint.append(n[1])
      if n[1] in connectedTreePoint and n[0] not in connectedTreePoint:
        connectedTree.append(n)
        connectedTreePoint.append(n[0])
      loop = False
      for p in connectedPoint:
        if p not in connectedTreePoint:
          loop = True
      
  return connectedTree   
       
    

def min_prim(graph, node='A', visited=[], minimum = 999999999):
  visited = edge_get(graph, node, visited, minimum)
  connectedPoint =[]
  connectedTree = []
  
  connectedPoint.append(node)
  loop = True
  
  while loop:
    for n in visited:
      if n[0] in connectedPoint or n[1] in connectedPoint:
        if n[0] in connectedPoint and n[0] in connectedPoint:
          loop = False
          for x in visited:
            if x[0] not in connectedPoint or x[1] not in connectedPoint:
              loop = True
        if loop == False:
          break
        if n[0] in connectedPoint and n[1] not in connectedPoint:
          connectedPoint.append(n[1])
          connectedTree.append(n)
          break
        elif n[1] in connectedPoint and n[0] not in connectedPoint:
          connectedPoint.append(n[0])
          connectedTree.append(n)
          break
        
  return connectedTree




   
















