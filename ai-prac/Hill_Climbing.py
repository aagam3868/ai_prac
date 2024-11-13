import random

# Objective function: We want to maximize this function
def objective_function(x):
    return -(x - 3) ** 2 + 10  # A simple parabola with maximum at x=3

# Hill Climbing algorithm
def hill_climbing(objective_function, start_point, step_size, max_iterations):
    current_point = start_point
    current_value = objective_function(current_point)
    
    for iteration in range(max_iterations):
        # Generate a neighboring point (move left or right by step size)
        neighbors = [current_point + step_size, current_point - step_size]
        
        # Evaluate the neighbors
        next_point = max(neighbors, key=objective_function)  # Select the neighbor with the best value
        next_value = objective_function(next_point)
        
        # If the neighbor improves the solution, move to that point
        if next_value > current_value:
            current_point = next_point
            current_value = next_value
            print(f"Iteration {iteration + 1}: x = {current_point:.4f}, f(x) = {current_value:.4f}")
        else:
            # No improvement, terminate
            print(f"No improvement after {iteration + 1} iterations. Stopping.")
            break
    
    return current_point, current_value

# Parameters for the Hill Climbing algorithm
start_point = random.uniform(-10, 10)  # Random starting point
step_size = 0.1  # Small step size
max_iterations = 100  # Limit on the number of iterations

# Run Hill Climbing
best_point, best_value = hill_climbing(objective_function, start_point, step_size, max_iterations)

# Output the result
print(f"\nBest point found: x = {best_point:.4f}, f(x) = {best_value:.4f}")
