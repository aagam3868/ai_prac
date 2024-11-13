# class AONode:
#     def __init__(self, name, heuristic):
#         self.name = name
#         self.heuristic = heuristic
#         self.children = []  # Children can be a list of sets, each set for an AND arc

#     def add_child(self, child_set):
#         self.children.append(child_set)

# def ao_star(node, graph):
#     if not node.children:
#         return node.heuristic
    
#     min_cost = float('inf')
#     best_child_set = None

#     for child_set in node.children:
#         cost = 0
#         for child_name in child_set:
#             child = graph[child_name]
#             cost += ao_star(child, graph)
        
#         if cost < min_cost:
#             min_cost = cost
#             best_child_set = child_set

#     return node.heuristic + min_cost

# # Example Graph for AO* (AND-OR graph)
# graph_ao = {
#     'A': AONode('A', 1),
#     'B': AONode('B', 6),
#     'C': AONode('C', 2),
#     'D': AONode('D', 0),
#     'E': AONode('E', 5),
#     'F': AONode('F', 4),
#     'G': AONode('G', 0)
# }

# # Define AND-OR relationships
# graph_ao['A'].add_child(['B', 'C'])
# graph_ao['B'].add_child(['D', 'E'])
# graph_ao['C'].add_child(['F', 'G'])

# # Apply AO* algorithm
# cost = ao_star(graph_ao['A'], graph_ao)
# print("Cost using AO*:", cost)



class AONode:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.children = []  # Children can be a list of sets, each set for an AND arc

    def add_child(self, child_set):
        self.children.append(child_set)

def ao_star(node, graph):
    if not node.children:
        return node.heuristic
    
    min_cost = float('inf')
    best_child_set = None

    for child_set in node.children:
        cost = 0
        for child_name in child_set:
            child = graph[child_name]
            cost += ao_star(child, graph)
        
        if cost < min_cost:
            min_cost = cost
            best_child_set = child_set

    return node.heuristic + min_cost

# User Input for AO* Algorithm
def user_input_ao_star():
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))

    for _ in range(num_nodes):
        node = input("Enter node name: ")
        heuristic = int(input(f"Enter heuristic value for {node}: "))
        graph[node] = AONode(node, heuristic)
        
    print("\nEnter AND-OR relationships:")
    for node in graph:
        num_sets = int(input(f"Enter the number of AND sets for {node}: "))
        for _ in range(num_sets):
            child_set = input(f"Enter the child nodes (space-separated) for {node}'s AND set: ").split()
            graph[node].add_child(child_set)

    root = input("\nEnter the root node: ")
    cost = ao_star(graph[root], graph)
    print(f"\nCost using AO* for root node {root}: {cost}")

# Call user input function for AO* algorithm
user_input_ao_star()
