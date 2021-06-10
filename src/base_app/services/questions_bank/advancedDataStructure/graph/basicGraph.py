# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 08:20:00 2018

@author: atanand
"""

#Graph

class Vertex:
    def __init__(self,name):
        self.name=name
        self.neighbors=list()
    
    def add_neighbor(self,v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = {}            
        