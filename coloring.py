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



def smallest(graph, vert, color, num = 1):
  numbers = [];
  print(color)
  print(vert)
  if vert in color:
    print("vert in color?")
    numbers.append(color[n])
  for n in graph[vert]:
    if n in color:
      print("n in color?")
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















