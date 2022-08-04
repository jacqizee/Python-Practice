class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}
    
    def get_edges(self):
        # OOP - Encapsulation
        return list(self.edges.keys())
    
    def add_edge(self, value, weight=0):
        self.edges[value] = weight