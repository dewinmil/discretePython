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
      count += 1
    n[1] = num
    currentTree.append(n)

  allTrees.append(currentTree)
  currentTree = []
  maxCount = count

  return allTrees
  


def is_proper_edge(graph):
  buff = []
  for n in graph:
    buff = []
    for x in graph[n]:
      for c in x:
        if type(c) is int:
          if c not in buff:
            buff.append(c)
          else:
            return False
          
  return True

def greedy(graph, order):
  return True   
