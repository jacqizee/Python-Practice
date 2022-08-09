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

    def find_path_by_value(self, starting, ending):
        to_trek = self.vertices[starting].get_edges()
        seen = set()
        while to_trek:
            current = to_trek.pop(0)
            seen.add(current)
            if current == ending:
                return True
            else:
                to_add = self.vertices[current].get_edges()
                to_trek += [vertex for vertex in to_add if vertex not in seen]
        return False
    
    def dfs(self, current_value, target_value, visited=None):
        if visited is None:
            visited = []
        
        visited.append(current_value)

        if current_value == target_value:
            return visited
        
        for neighbor in self.vertices[current_value].get_edges():
            if neighbor not in visited:
                path = self.dfs(neighbor, target_value, visited)
                if path:
                    return path

    def bfs(self, start_value, target_value):
        queue = [[start_value]]
        visited = set()

        while queue:
            path = queue.pop(0)
            current_value = path[-1]
            visited.add(current_value)
            
            for neighbor in self.vertices[current_value].get_edges():
                if neighbor == target_value:
                    return path + [neighbor]
                if neighbor not in visited:
                    queue.append(path + [neighbor])