# # Tic Tac Toe game

# # Display the board
# def display_board(board):
#     print("\n")
#     print(f" {board[0]} | {board[1]} | {board[2]} ")
#     print("---|---|---")
#     print(f" {board[3]} | {board[4]} | {board[5]} ")
#     print("---|---|---")
#     print(f" {board[6]} | {board[7]} | {board[8]} ")
#     print("\n")

# # Check for a winner
# def check_winner(board, player):
#     # Winning combinations
#     win_combinations = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
#         [0, 4, 8], [2, 4, 6]              # diagonals
#     ]
#     for combination in win_combinations:
#         if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
#             return True
#     return False

# # Check for a tie
# def check_tie(board):
#     return all(cell != " " for cell in board)

# # Main function to play the game
# def play_game():
#     board = [" " for _ in range(9)]  # Initialize an empty board
#     current_player = "X"  # Starting player

#     # Game loop
#     while True:
#         display_board(board)
        
#         # Take input from player
#         try:
#             move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
#             if board[move] != " ":
#                 print("Invalid move! Cell already taken. Try again.")
#                 continue
#         except (ValueError, IndexError):
#             print("Invalid input! Please enter a number from 1 to 9.")
#             continue

#         # Update the board
#         board[move] = current_player

#         # Check for a winner
#         if check_winner(board, current_player):
#             display_board(board)
#             print(f"Player {current_player} wins!")
#             break

#         # Check for a tie
#         if check_tie(board):
#             display_board(board)
#             print("It's a tie!")
#             break

#         # Switch players
#         current_player = "O" if current_player == "X" else "X"

# # Start the game
# if __name__ == "__main__":
#     play_game()






def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def is_board_full(board):
    for row in board:
        if any([cell == " " for cell in row]):
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        
        try:
            row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue
        
        if board[row][col] != " ":
            print("That cell is already taken! Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
