from collections import defaultdict

def makeGraph(links):
  graph = defaultdict(list)
  for link in links:
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])
  
  return graph


print(makeGraph([(1,2),(1,4),(2,3),(3,4)]))