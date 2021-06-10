
#adjecency list
g = {'A':set(['B','C']),
     'B':set(['A','D','E']),
     'C':set(['A','F']),
     'D':set(['B']),
     'E':set(['B','F']),
     'F':set(['C','E']) }
     
     
     
def dfs(g,start):
    visited = set()
    stack =[start]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            
            stack.extend(g[vertex] - visited)
    return visited


print(dfs(g,'A'))     



def bfs(g,start):
    visited = set()
    queue =[start]
    
    while queue:
        vertex = queue.pop(0)
        
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(g[vertex] - visited)
            
    return visited

print(bfs(g,'A'))