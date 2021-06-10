
from enum import Enum
from collections import OrderedDict

class State(Enum):
    unvisited =1
    visited =2
    visiting =3

class Node:
    
    def __init__(self,num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict() #key:Node val:weight
    
    
    def __str__(self):
        return str(self.num)
    
class Graph:
    def __init__(self):
        self.nodes = OrderedDict()
        
    
    def add_node(self,num):
        node = Node(num)
        self.nodes[num] = node
        return node
    
    def add_edge(self,source,dest,weight=0):
        
        if source not in self.nodes:
            self.add_node(source)
            
        if dest not in self.nodes:
            self.add_node(dest)
            
        self.nodes[source].adjacent[self.nodes[dest]] = weight
        
def dfs(g,start):
    visited = set()
    stack =[start]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            
            stack.extend(g[vertex] - visited)
    return visited

    
    
g = Graph()        
g.add_edge('A','B',1)      
g.add_edge('A','C',1)      

g.add_edge('B','A',1)      
g.add_edge('B','D',1)      
g.add_edge('B','E',1)      

g.add_edge('C','A',1)      
g.add_edge('C','F',1)  

g.add_edge('D','B',1)      

g.add_edge('E','B',1)      
g.add_edge('E','F',1)  

g.add_edge('F','C',1)      
g.add_edge('F','E',1)  

print(g.nodes)


print(dfs(g,'A'))
    
"""
g.add_edge(1,2,3)

g = {'A':set(['B','C']),
     'B':set(['A','D','E']),
     'C':set(['A','F']),
     'D':set(['B']),
     'E':set(['B','F']),
     'F':set(['C','E'])}

print(g.nodes)
"""
     
