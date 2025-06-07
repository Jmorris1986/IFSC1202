pip install python-chess
import chess
import chess.engine

def main():
    print("Welcome to Chess: Person vs Computer!")
    print("Type 'exit' to quit the game at any time.\n")

    # Initialize the chess board
    board = chess.Board()
    player_score = 0
    computer_score = 0

    # Initialize the chess engine (Stockfish)
    with chess.engine.SimpleEngine.popen_uci("/usr/bin/stockfish") as engine:
        while not board.is_game_over():
            print(board)
            print("\nYour move (e.g., e2e4): ", end="")
            player_move = input().strip()

            if player_move.lower() == "exit":
                print("Game exited.")
                break

            try:
                move = chess.Move.from_uci(player_move)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    print("Illegal move. Try again.")
                    continue
            except ValueError:
                print("Invalid move format. Try again.")
                continue

            if board.is_game_over():
                break

            # Computer's move
            print("\nComputer is thinking...")
            result = engine.play(board, chess.engine.Limit(time=1.0))
            board.push(result.move)
            print(f"Computer played: {result.move}\n")

        # Game over
        print("\nGame Over!")
        print(board)
        if board.is_checkmate():
            if board.turn:  # If it's the player's turn, computer won
                print("Checkmate! Computer wins!")
                computer_score += 1
            else:  # If it's the computer's turn, player won
                print("Checkmate! You win!")
                player_score += 1
        elif board.is_stalemate():
            print("Stalemate! It's a draw.")
        elif board.is_insufficient_material():
            print("Draw due to insufficient material.")
        elif board.is_seventyfive_moves():
            print("Draw due to 75-move rule.")
        elif board.is_fivefold_repetition():
            print("Draw due to fivefold repetition.")

        print(f"\nFinal Score:\nPlayer: {player_score}\nComputer: {computer_score}")

if __name__ == "__main__":
    main()