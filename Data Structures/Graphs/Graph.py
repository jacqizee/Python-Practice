class Graph:
    def __init__(self, directed=False):
        # specify whether the graph is directed or not
        self.directed = directed
        self.graph_vertices = {}
    
    def add_vertex(self, vertex):
        self.graph_vertices[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight):
        self.graph_vertices[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_vertices[to_vertex.value].add_edge(from_vertex.value, weight)