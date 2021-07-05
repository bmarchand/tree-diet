from itertools import combinations
import random
import numpy as np


# IMPORTANT CLASSES

class Graph:
    """
    simple graph class, just used for producing its adjacency dictionary.
    """

    def __init__(self, list_vertices=None):
        """
        Graph constructor: optionally takes a list of vertices as input.

        :param list_vertices: Optional list of vertices for the graph, defaults to None
        :type list_vertices: list, optional
        """

        self.adj = {}
        self.n = 0

        if list_vertices:
            self.n = len(list_vertices)

            for i in list_vertices:
                self.adj[i] = set()

    def add_vertex(self, i):
        """
        Adds a vertex to the graph

        :param i: Integer to add as new vertex of the graph. If the vertex is already present nothing happens.
        :type i: **int**
        """

        try:
            self.adj[i]
        except KeyError:
            self.adj[i] = set()
            self.n += 1
            

    def add_edge(self, i, j):
        """
        Adds an edge between two vertices
        """

        if i >= self.n:
            return
        if i == j:
            return

        self.adj[i].add(j)
        self.adj[j].add(i)


class Bag:
    """
    Bag class for constructing tree decompositions.
    There is no tree decomposition class. A tree decomposition
    will be represented by its root bag. 
    """
    def __init__(self, vertices):

        self.vertices = vertices
        self.children = []

    def add_child(self, child):

        self.children.append(child)

    def make_nice(self, child):

        self.children.remove(child)

        inter = [u for u in self.vertices if u in child.vertices]
        
        to_introduce = [v for v in self.vertices if v not in inter]
        to_forget = [v for v in child.vertices if v not in inter]

        seq = []

        cur_vertices = self.vertices

        for u in to_introduce[::-1]:

            if u == to_introduce[-1]:
                continue

            seq.append(py_bag([v for v in cur_vertices if v!= u]))

            cur_vertices = [v for v in cur_vertices if v!= u]

        if len(self.vertices) > 0:
            seq.append(py_bag(list(inter)))
        cur_vertices = inter

        for u in to_forget[::-1]:

            if u == to_forget[0]:
                continue

            cur_vertices.append(u)
            seq.append(py_bag([u for u in cur_vertices]))


    
        self.add_child(seq[0])
        for k in range(1,len(seq),1):
            seq[k-1].add_child(seq[k])

        seq[-1].add_child(child) 

    def dupli_nice(self):

        if len(self.children) > 2:

            duplicate = py_bag([u for u in self.vertices])

            for i in range(1, len(self.children),1):
                duplicate.add_child(self.children[i])

            self.children = [self.children[0]]

            self.add_child(duplicate)
            

def nicify(R):

    queue = [R]

    while len(queue) > 0:

        u = queue.pop()

        children = [c for c in u.children]
        for c in children:
            queue.append(c)
            u.make_nice(c)        

    queue = [R]

    while len(queue) > 0:

        u = queue.pop()

        n_children = len(u.children)

        if n_children > 2:

            for _ in range(n_children-2):
                u.dupli_nice()

        for c in u.children:
            queue.append(c)           
 
    return R
   


def recurse_print(b, depth, tags=None):

    for _ in range(depth):
        print("   ", end="")

    if tags:
        print("tag ", tags[b], end=" ")    

    print(b, b.vertices)
    for c in b.children:
        recurse_print(c, depth+1, tags=tags)    
