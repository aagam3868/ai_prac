import heapq

# Graph represented as an adjacency list with heuristic values
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('E', 12)],
    'C': [('F', 7)],
    'D': [('G', 2)],
    'E': [('G', 5)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values (estimated cost to reach the goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0  # Goal node
}

def best_first_search(graph, start, goal):
    # Priority queue to store nodes with their heuristic value
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    
    # Set to track visited nodes
    visited = set()
    
    # To store the path
    path = []

    while open_list:
        # Get the node with the smallest heuristic value
        _, current_node = heapq.heappop(open_list)
        
        # Mark the node as visited
        visited.add(current_node)
        path.append(current_node)

        # If goal is reached, return the path
        if current_node == goal:
            return path

        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    return None  # No path found

# Example usage
start_node = 'A'
goal_node = 'G'
path = best_first_search(graph, start_node, goal_node)
print("Path:", path)
