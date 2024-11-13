# def dfs_hardcoded(graph, node, visited=None):
#     if visited is None:
#         visited = set()  # Initialize the visited set if not already provided
    
#     if node not in visited:
#         print(node, end=" ")  # Print the visited node
#         visited.add(node)  # Mark the node as visited
        
#         # Recursively visit each unvisited neighbor
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 dfs_hardcoded(graph, neighbor, visited)

# # Hardcoded graph as an adjacency list
# graph_hardcoded = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# print("DFS traversal of the hardcoded graph starting from node 'A':")
# dfs_hardcoded(graph_hardcoded, 'A')





def dfs_user(graph, start):
    visited = set()  # Keep track of visited nodes
    stack = [start]  # Initialize stack with the start node
    
    while stack:
        node = stack.pop()  # Pop a node from the top of the stack
        if node not in visited:
            print(node, end=" ")  # Print the visited node
            visited.add(node)  # Mark the node as visited
            
            # Add all unvisited neighbors to the stack
            # Reverse the neighbors for a more intuitive order (left-to-right)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Getting user input to create the graph
def create_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    
    for _ in range(num_nodes):
        node = input("Enter node: ")
        neighbors = input(f"Enter neighbors of {node} (separated by space): ").split()
        graph[node] = neighbors  # Add node and its neighbors to the graph
    
    return graph

# Running DFS on a user-input graph
print("Enter the graph details:")
graph_user = create_graph()
start_node = input("Enter the start node: ")

print(f"\nDFS traversal of the user-input graph starting from node '{start_node}':")
dfs_user(graph_user, start_node)
