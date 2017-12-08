def is_proper(graph, color):
  for n in graph:
    for c in graph[n]:
      if color[n] == color[c]:
        return False
  return True

  

def three_color(graph):
  allTrees = []
  currentTree = {}
  setTree = []
  for n in graph:
    currentTree.update({n : 1})

  r = currentTree.copy()
  allTrees.append(r);
  breakBool = False
  loop = True
  for num in range(0, len(graph) * len(graph) * len(graph)):
    setTree =[]
    for n in currentTree:
      if currentTree[n] <3:
        currentTree[n] += 1
        r = currentTree.copy()
        allTrees.append(r);
        break
      else:
        currentTree[n] = 1
  
  return allTrees



def is_three_color(graph):
  myList = three_color(graph)
  for n in myList:
    boolean = is_proper(graph, n)
    if boolean == True:
      return True
  return False





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



def smallest(graph, vert, color, num = 1):
  numbers = [];
  if vert in color:
    numbers.append(color[n])
  for n in graph[vert]:
    if n in color:
      numbers.append(color[n])
  loop = True
  while loop:
    if num in numbers:
      num += 1
    else:
      loop = False
      return num

def greedy(graph, order, color = {}, num = 1):
  if color == {}:
    color = {order[0] : 1}
    num = 2

  for o in order:
    if o not in color:
      num = smallest(graph, o, color);
      color[o] = num
      num += 1
    for n in graph:
      if n == o:
        for x in graph[n]:
          if x not in color:
            num = smallest(graph, x, color)
            color[x] = num
           

  return sorted(color.items())















