def is_proper(graph, color):
  for n in graph:
    for c in graph[n]:
      if color[n] == color[c]:
        return False
  return True



def three_color(graph):
  allTrees = []
  currentTree =[]
  num = 1
  count = 0
  currentPos = 0

  for n in graph:
    if maxCount == 0:
      count++
    n[1] = num
    currentTree.append(n)

  allTrees.append(currentTree)
  currentTree = []
  maxCount = count

  return allTrees
  


def is_proper_edge(graph):
  


def greedy(graph, order):
   
