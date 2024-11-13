import numpy as np
import random

# Simple environment (4x4 grid)
# 0 = Empty, 1 = Goal, -1 = Obstacle
grid = [
    [0, 0, 0, 1],
    [0, -1, 0, 0],
    [0, -1, 0, 0],
    [0, 0, 0, 0]
]

# Q-learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 1.0  # Exploration rate
epsilon_decay = 0.99
min_epsilon = 0.1

# Actions: 0 = Left, 1 = Down, 2 = Right, 3 = Up
actions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # (dx, dy)

# Q-table initialization
q_table = np.zeros((4, 4, 4))  # 4x4 grid, 4 possible actions

# Reward function
def reward(state):
    if grid[state[0]][state[1]] == 1:  # Goal
        return 10
    elif grid[state[0]][state[1]] == -1:  # Obstacle
        return -10
    return -1  # Default step cost

# Move agent in the grid
def move(state, action):
    x, y = state
    dx, dy = actions[action]
    new_state = (max(0, min(3, x + dx)), max(0, min(3, y + dy)))  # Keep within bounds
    return new_state

# Q-learning algorithm
def q_learning(epochs=1000):
    global epsilon

    for _ in range(epochs):
        state = (0, 0)  # Start from the top-left corner
        done = False
        
        while not done:
            if random.uniform(0, 1) < epsilon:
                action = random.choice([0, 1, 2, 3])  # Explore
            else:
                action = np.argmax(q_table[state[0], state[1]])  # Exploit
            
            next_state = move(state, action)
            r = reward(next_state)
            q_table[state[0], state[1], action] = q_table[state[0], state[1], action] + alpha * (
                r + gamma * np.max(q_table[next_state[0], next_state[1]]) - q_table[state[0], state[1], action]
            )
            
            state = next_state
            
            if grid[state[0]][state[1]] == 1:  # Reached goal
                done = True
        
        epsilon = max(min_epsilon, epsilon * epsilon_decay)  # Decay epsilon

# Run Q-learning
q_learning()

# Display learned Q-values
print("Learned Q-table:")
print(q_table)
