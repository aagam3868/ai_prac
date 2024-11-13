# import heapq

# class Node:
#     def __init__(self, name, parent=None, g=0, h=0):
#         self.name = name
#         self.parent = parent
#         self.g = g  # Cost from start to this node
#         self.h = h  # Heuristic cost (estimated cost to goal)
#         self.f = g + h  # Total cost (g + h)

#     def __lt__(self, other):
#         return self.f < other.f

# def a_star(graph, start, goal, h):
#     open_list = []
#     closed_list = set()
    
#     start_node = Node(start, g=0, h=h[start])
#     heapq.heappush(open_list, start_node)

#     while open_list:
#         current_node = heapq.heappop(open_list)

#         if current_node.name == goal:
#             path = []
#             while current_node:
#                 path.append(current_node.name)
#                 current_node = current_node.parent
#             return path[::-1]  # Return reversed path

#         closed_list.add(current_node.name)

#         for neighbor, cost in graph[current_node.name].items():
#             if neighbor in closed_list:
#                 continue
            
#             g = current_node.g + cost
#             h_cost = h[neighbor]
#             neighbor_node = Node(neighbor, parent=current_node, g=g, h=h_cost)

#             heapq.heappush(open_list, neighbor_node)

#     return None  # Return None if no path found

# # Example Graph and Heuristic
# graph = {
#     'A': {'B': 1, 'C': 3},
#     'B': {'D': 3, 'E': 12},
#     'C': {'F': 3},
#     'D': {},
#     'E': {'G': 2},
#     'F': {'E': 1},
#     'G': {}
# }

# # Heuristic (h) values
# h = {
#     'A': 7,
#     'B': 6,
#     'C': 2,
#     'D': 3,
#     'E': 4,
#     'F': 6,
#     'G': 0  # Goal node has heuristic value 0
# }

# # Find path using A* algorithm
# path = a_star(graph, 'A', 'G', h)
# print("Path using A*:", path)





import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g  # Cost from start to this node
        self.h = h  # Heuristic cost (estimated cost to goal)
        self.f = g + h  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def a_star(graph, start, goal, h):
    open_list = []
    closed_list = set()
    
    start_node = Node(start, g=0, h=h[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        closed_list.add(current_node.name)

        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_list:
                continue
            
            g = current_node.g + cost
            h_cost = h[neighbor]
            neighbor_node = Node(neighbor, parent=current_node, g=g, h=h_cost)

            heapq.heappush(open_list, neighbor_node)

    return None  # Return None if no path found

# User Input for A* Algorithm
def user_input_a_star():
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))

    for _ in range(num_nodes):
        node = input("Enter node name: ")
        graph[node] = {}
        num_neighbors = int(input(f"Enter the number of neighbors for node {node}: "))
        for _ in range(num_neighbors):
            neighbor = input(f"Enter neighbor name for {node}: ")
            cost = int(input(f"Enter cost to {neighbor}: "))
            graph[node][neighbor] = cost

    h = {}
    print("\nEnter heuristic values (h) for each node:")
    for node in graph:
        h[node] = int(input(f"Heuristic value for {node}: "))

    start = input("\nEnter the start node: ")
    goal = input("Enter the goal node: ")

    path = a_star(graph, start, goal, h)
    print("\nPath using A*:", path if path else "No path found.")

# Call user input function for A* algorithm
user_input_a_star()
