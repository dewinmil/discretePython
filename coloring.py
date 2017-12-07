def is_proper(graph, color):
  adjacent= [];
  for n in graph:
    for c in graph[n]:
      if color[n] == color[c]:
        return False
  return True


