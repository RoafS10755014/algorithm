# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['C', 'E'],
    'C' : ['D', 'F'],
    'D' : ['F'],
    'E' : [],
    'F' : []
}


visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print ('-->',node, end='')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print('DFS: ', end='')
dfs(visited, graph, 'A')
print()


graph = {
    'A' : ['B','C'],
    'B' : ['C', 'E'],
    'C' : ['D', 'F'],
    'D' : ['F'],
    'E' : [],
    'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print ('-->',s, end = "") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print('BFS: ', end='')
bfs(visited, graph, 'A')
