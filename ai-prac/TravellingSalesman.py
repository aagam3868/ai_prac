# from itertools import permutations

# # Function to calculate the total distance of a given tour
# def calculate_total_distance(tour, graph):
#     total_distance = 0
#     n = len(tour)
#     for i in range(n):
#         total_distance += graph[tour[i]][tour[(i + 1) % n]]  # Sum the distances between consecutive cities
#     return total_distance

# # Function to solve the TSP using brute force
# def travelling_salesman(graph):
#     n = len(graph)
#     cities = list(range(n))  # List of all cities
#     min_distance = float('inf')  # Initialize with infinity
#     best_tour = None

#     # Generate all permutations (tours) of the cities except the first (as it is the starting point)
#     for tour in permutations(cities[1:]):
#         current_tour = [0] + list(tour)  # Start the tour at city 0
#         current_distance = calculate_total_distance(current_tour, graph)

#         # Update the minimum distance and best tour if current tour is shorter
#         if current_distance < min_distance:
#             min_distance = current_distance
#             best_tour = current_tour

#     return best_tour, min_distance

# # Example graph represented as a 2D matrix (adjacency matrix)
# # graph[i][j] represents the distance from city i to city j
# graph = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]

# # Main function
# def main():
#     best_tour, min_distance = travelling_salesman(graph)
    
#     print("Best Tour:", best_tour)
#     print("Minimum Distance:", min_distance)

# # Run the main function
# if __name__ == "__main__":
#     main()


from itertools import permutations

# Function to calculate the total distance of a given tour
def calculate_total_distance(tour, graph):
    total_distance = 0
    n = len(tour)
    for i in range(n):
        total_distance += graph[tour[i]][tour[(i + 1) % n]]  # Sum the distances between consecutive cities
    return total_distance

# Function to solve the TSP using brute force
def travelling_salesman(graph):
    n = len(graph)
    cities = list(range(n))  # List of all cities
    min_distance = float('inf')  # Initialize with infinity
    best_tour = None

    # Generate all permutations (tours) of the cities except the first (as it is the starting point)
    for tour in permutations(cities[1:]):
        current_tour = [0] + list(tour)  # Start the tour at city 0
        current_distance = calculate_total_distance(current_tour, graph)

        # Update the minimum distance and best tour if current tour is shorter
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = current_tour

    return best_tour, min_distance

# Function to input graph data from the user
def input_graph():
    n = int(input("Enter the number of cities: "))
    graph = []
    
    print(f"Enter the distance matrix (each row should contain distances from city i to other cities):")
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        graph.append(row)
    
    return graph

# Main function
def main():
    graph = input_graph()  # Get graph input from user
    best_tour, min_distance = travelling_salesman(graph)
    
    print("\nBest Tour:", best_tour)
    print("Minimum Distance:", min_distance)

# Run the main function
if __name__ == "__main__":
    main()
