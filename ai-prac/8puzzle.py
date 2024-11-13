# from queue import PriorityQueue

# # Define the goal state of the puzzle
# GOAL_STATE = [[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 0]]  # Using 0 to represent the blank space

# # Helper function to find the position of the blank tile (0)
# def find_blank_position(state):
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] == 0:
#                 return i, j

# # Function to calculate the Manhattan distance heuristic
# def manhattan_distance(state):
#     distance = 0
#     for i in range(3):
#         for j in range(3):
#             value = state[i][j]
#             if value != 0:
#                 target_x = (value - 1) // 3
#                 target_y = (value - 1) % 3
#                 distance += abs(i - target_x) + abs(j - target_y)
#     return distance

# # Function to generate possible moves from the current state
# def get_neighbors(state):
#     neighbors = []
#     x, y = find_blank_position(state)
#     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left

#     for dx, dy in directions:
#         new_x, new_y = x + dx, y + dy
#         if 0 <= new_x < 3 and 0 <= new_y < 3:
#             # Swap blank with the neighboring tile
#             new_state = [row[:] for row in state]
#             new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
#             neighbors.append(new_state)
#     return neighbors

# # Function to convert state to tuple for storing in visited set
# def state_to_tuple(state):
#     return tuple(tuple(row) for row in state)

# # A* search algorithm to solve the 8-puzzle problem
# def a_star(start_state):
#     open_list = PriorityQueue()
#     open_list.put((0, start_state, []))
#     visited = set()

#     while not open_list.empty():
#         cost, current_state, path = open_list.get()
#         visited.add(state_to_tuple(current_state))

#         if current_state == GOAL_STATE:
#             return path + [current_state]

#         for neighbor in get_neighbors(current_state):
#             if state_to_tuple(neighbor) not in visited:
#                 new_cost = len(path) + 1 + manhattan_distance(neighbor)
#                 open_list.put((new_cost, neighbor, path + [current_state]))

#     return None  # Return None if no solution is found

# # Print each step of the solution
# def print_solution(path):
#     for i, step in enumerate(path):
#         print(f"Step {i}:")
#         for row in step:
#             print(" ".join(map(str, row)))
#         print("\n")

# # Initial state of the puzzle
# start_state = [
#     [1, 2, 3],
#     [4, 0, 6],
#     [7, 5, 8]
# ]

# solution = a_star(start_state)

# if solution:
#     print("Solution found:")
#     print_solution(solution)
# else:
#     print("No solution exists for this initial state.")



import numpy as np
from heapq import heappop, heappush

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.blank_tile = self.find_blank()
        self.moves = moves
        self.previous = previous

    def find_blank(self):
        return tuple(np.argwhere(self.board == 0)[0])

    def is_goal(self):
        return np.array_equal(self.board, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))

    def get_neighbors(self):
        neighbors = []
        x, y = self.blank_tile
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = self.board.copy()
                # Swap the blank tile with the adjacent tile
                new_board[x, y], new_board[new_x, new_y] = new_board[new_x, new_y], new_board[x, y]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

    def __lt__(self, other):
        return (self.moves + self.manhattan_distance()) < (other.moves + other.manhattan_distance())

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    target_x = (self.board[i][j] - 1) // 3
                    target_y = (self.board[i][j] - 1) % 3
                    distance += abs(target_x - i) + abs(target_y - j)
        return distance

def a_star(initial_board):
    initial_state = PuzzleState(initial_board)
    if initial_state.is_goal():
        return initial_state

    priority_queue = []
    heappush(priority_queue, initial_state)
    visited = set()

    while priority_queue:
        current_state = heappop(priority_queue)
        visited.add(tuple(current_state.board.flatten()))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board.flatten()) in visited:
                continue
            if neighbor.is_goal():
                return neighbor
            heappush(priority_queue, neighbor)

    return None

def print_solution(solution):
    path = []
    while solution:
        path.append(solution.board)
        solution = solution.previous
    for step in reversed(path):
        print(step, "\n")

def main():
    initial_board = np.array([[1, 2, 3],
                              [4, 0, 5],
                              [7, 8, 6]])

    solution = a_star(initial_board)
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
