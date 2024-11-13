# Graph Coloring using Greedy Algorithm

# Function to perform graph coloring
def greedy_coloring(graph):
    # Number of vertices in the graph
    n = len(graph)
    
    # List to store the color assigned to each vertex
    # -1 represents that no color is assigned yet
    result = [-1] * n
    
    # Assign the first color (0) to the first vertex
    result[0] = 0
    
    # A temporary array to keep track of the colors assigned to the adjacent vertices
    available_colors = [False] * n
    
    # Assign colors to the remaining vertices
    for vertex in range(1, n):
        # Check the colors of the adjacent vertices and mark them as unavailable
        for adjacent in graph[vertex]:
            if result[adjacent] != -1:
                available_colors[result[adjacent]] = True
        
        # Find the first available color
        color = 0
        while color < n and available_colors[color]:
            color += 1
        
        # Assign the found color to the current vertex
        result[vertex] = color
        
        # Reset the values of available_colors for the next vertex
        available_colors = [False] * n
    
    # Print the result
    for vertex in range(n):
        print(f"Vertex {vertex} --->  Color {result[vertex]}")

# Example graph represented as an adjacency list
# Each index represents a vertex, and the list at each index contains its adjacent vertices
graph = [
    [1, 2],  # Vertex 0 is adjacent to 1 and 2
    [0, 2],  # Vertex 1 is adjacent to 0 and 2
    [0, 1, 3],  # Vertex 2 is adjacent to 0, 1, and 3
    [2]  # Vertex 3 is adjacent to 2
]

# Call the greedy_coloring function with the graph
greedy_coloring(graph)
