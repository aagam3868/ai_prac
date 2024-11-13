# from collections import deque

# def bfs_hardcoded(graph, start):
#     visited = set()  # Keep track of visited nodes
#     queue = deque([start])  # Initialize a queue with the start node
    
#     while queue:
#         node = queue.popleft()  # Pop a node from the front of the queue
#         if node not in visited:
#             print(node, end=" ")  # Print the visited node
#             visited.add(node)  # Mark the node as visited
            
#             # Add all unvisited neighbors to the queue
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)

# # Hardcoded graph as an adjacency list
# graph_hardcoded = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# print("BFS traversal of the hardcoded graph starting from node 'A':")
# bfs_hardcoded(graph_hardcoded, 'A')

from collections import deque

def bfs_user(graph, start):
    visited = set()  # Keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the start node
    
    while queue:
        node = queue.popleft()  # Pop a node from the front of the queue
        if node not in visited:
            print(node, end=" ")  # Print the visited node
            visited.add(node)  # Mark the node as visited
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Getting user input to create the graph
def create_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    
    for _ in range(num_nodes):
        node = input("Enter node: ")
        neighbors = input(f"Enter neighbors of {node} (separated by space): ").split()
        graph[node] = neighbors  # Add node and its neighbors to the graph
    
    return graph

# Running BFS on a user-input graph
print("Enter the graph details:")
graph_user = create_graph()
start_node = input("Enter the start node: ")

print(f"\nBFS traversal of the user-input graph starting from node '{start_node}':")
bfs_user(graph_user, start_node)
