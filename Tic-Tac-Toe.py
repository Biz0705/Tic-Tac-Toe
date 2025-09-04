board = [" " for _ in range(9)]

def display_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def player_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, choose a position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid position. Please choose 1-9.")
            elif board[move] != " ":
                print("That spot is already taken. Try again.")
            else:
                board[move] = player
                break
        except ValueError:
            print("Please enter a valid number.")

def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in winning_combinations)  

def check_tie(board):
    return " " not in board

def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"
   
    while True:
        display_board(board)
        player_move(current_player, board)
       
        # Check for winner
        if check_winner(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            break
       
        # Check for tie
        if check_tie(board):
            display_board(board)
            print("It's a tie! 🤝")
            break
       
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()    