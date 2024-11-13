from collections import deque

def water_jug_bfs(m, n, d):
    queue = deque([(0, 0)])  # Start with both jugs empty
    visited = set([(0, 0)])  # Track visited states
    steps = []  # Track the sequence of steps
    
    while queue:
        x, y = queue.popleft()
        steps.append((x, y))
        
        # If either jug has exactly d liters, return the steps
        if x == d or y == d:
            return steps
        
        # Generate all possible next states
        possible_states = [
            (m, y),  # Fill Jug1
            (x, n),  # Fill Jug2
            (0, y),  # Empty Jug1
            (x, 0),  # Empty Jug2
            (x - min(x, n - y), y + min(x, n - y)),  # Pour Jug1 -> Jug2
            (x + min(y, m - x), y - min(y, m - x))   # Pour Jug2 -> Jug1
        ]
        
        for state in possible_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
    
    return []  # Return empty list if no solution is found

# User input and function call
def user_input_water_jug():
    m = int(input("Enter capacity of Jug1: "))
    n = int(input("Enter capacity of Jug2: "))
    d = int(input("Enter the goal amount of water to measure: "))
    
    if d > max(m, n):
        print("No solution: The goal exceeds both jug capacities.")
        return
    
    solution = water_jug_bfs(m, n, d)
    
    if solution:
        print("\nSteps to measure", d, "liters of water:")
        for step, (jug1, jug2) in enumerate(solution):
            print(f"Step {step}: Jug1 = {jug1} liters, Jug2 = {jug2} liters")
    else:
        print("\nNo solution found.")

# Call the function
user_input_water_jug()
