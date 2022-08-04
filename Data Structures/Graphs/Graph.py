class Graph:
    def __init__(self, directed=False):
        # specify whether the graph is directed or not
        self.directed = directed
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex.value] = vertex

    def add_edge(self, starting, ending, weight=0):
        self.vertices[starting.value].add_edge(ending.value, weight)
        if not self.directed:
            self.vertices[ending.value].add_edge(starting.value, weight)

    def find_path(self, starting, ending):
        to_trek = self.vertices[starting.value].get_edges()
        seen = set()
        while to_trek:
            current = to_trek.pop(0)
            seen.add(current)
            if current == ending.value:
                return True
            else:
                to_add = self.vertices[current].get_edges()
                to_trek += [vertex for vertex in to_add if vertex not in seen]
        return False