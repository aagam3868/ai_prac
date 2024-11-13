# Depth-Limited Search function
def depth_limited_search(graph, start, goal, limit):
    def dls_recursive(node, goal, limit, path, visited):
        # Add the node to the path
        path.append(node)
        visited.add(node)
        
        # If the goal is reached, return the path
        if node == goal:
            return path
        
        # If the limit is reached, return None
        if limit <= 0:
            path.pop()  # Backtrack
            return None
        
        # Recur for all neighbors if limit is not yet reached
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                result = dls_recursive(neighbor, goal, limit - 1, path, visited)
                if result is not None:
                    return result
        
        # Backtrack if no path is found
        path.pop()
        return None

    # Initialize path and visited set
    path = []
    visited = set()
    return dls_recursive(start, goal, limit, path, visited)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['I'],
    'H': [],
    'I': []
}

# Input for start, goal, and depth limit
start_node = 'A'
goal_node = 'I'
depth_limit = 3

# Perform Depth-Limited Search
result = depth_limited_search(graph, start_node, goal_node, depth_limit)

# Output the result
if result:
    print("Path found:", result)
else:
    print("No path found within depth limit")
