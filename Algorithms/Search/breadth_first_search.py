# BFS can be achieved with the help of a queue
# runtime of O(E+V)

def bfs(graph, start_value, target_value):
    queue = [[start_value]]
    visited = set()

    while queue:
        path = queue.pop(0)
        current_value = path[-1]
        visited.add(current_value)

        for adjacent_value in graph[current_value]:
            if adjacent_value == target_value:
                return path + [adjacent_value]
            if adjacent_value not in visited:
                queue.append(path + [current_value])