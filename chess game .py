import chess
import chess.engine
import random


def main():
    # Initialize the chess board
    board = chess.Board()
    moves_record = []  # To record all moves
    print("Welcome to Chess! You are playing as White.")
    print(board)

    while not board.is_game_over():
        if board.turn:  # White's turn (Human)
            try:
                user_move = input("Enter your move (e.g., e2e4): ")
                move = chess.Move.from_uci(user_move)
                if move in board.legal_moves:
                    board.push(move)
                    moves_record.append(f"White: {user_move}")
                    print("\nYour move:")
                    print(board)
                else:
                    print("Invalid move. Please try again.")
            except Exception as e:
                print("Error:", e)
                print("Please enter a valid move in UCI format (e.g., e2e4).")
        else:  # Black's turn (Computer)
            print("\nComputer's turn...")
            legal_moves = list(board.legal_moves)
            computer_move = random.choice(legal_moves)  # Random legal move
            board.push(computer_move)
            moves_record.append(f"Black: {computer_move.uci()}")
            print("Computer played:")
            print(board)

    # Game over
    print("\nGame Over!")
    print("Final Board Position:")
    print(board)

    # Determine the result
    if board.is_checkmate():
        if board.turn:  # If it's White's turn and checkmate, Black wins
            print("Checkmate! Black (Computer) wins!")
            winner = "Black (Computer)"
        else:  # If it's Black's turn and checkmate, White wins
            print("Checkmate! White (You) win!")
            winner = "White (You)"
    elif board.is_stalemate():
        print("It's a stalemate! The game is a draw.")
        winner = "Draw"
    elif board.is_insufficient_material():
        print("Insufficient material! The game is a draw.")
        winner = "Draw"
    elif board.is_seventyfive_moves():
        print("75-move rule applied! The game is a draw.")
        winner = "Draw"
    elif board.is_fivefold_repetition():
        print("Fivefold repetition rule applied! The game is a draw.")
        winner = "Draw"
    else:
        print("The game ended for an unknown reason.")
        winner = "Unknown"

    # Print the recorded moves
    print("\nMoves Record:")
    for move in moves_record:
        print(move)

    # Print the winner
    print(f"\nWinner: {winner}")

if __name__ == "__main__":
    main()