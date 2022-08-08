# DFS can be achieved with the help of either a stack or recursion

# Recursive Method - more common
def dfs(graph, current_vertex, target_vertex, visited=None):
    if visited is None:
        visited = []

    visited.append(current_vertex)

    if current_vertex == target_vertex:
        return visited

    for adjacent_vertex in graph[current_vertex]:
        if adjacent_vertex not in visited:
            path = dfs(adjacent_vertex)
        if path:
            return path