import random

def print_board(board):
    print(board)

def get_human_move():
    move = input("Enter your move in UCI format (e.g., e2e4): ")
    return move

def get_computer_move(board):
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)

def main():
    player_name = input("Enter your name: ")
    board = chess.Board() # type: ignore
    human_score = 0
    computer_score = 0

    while not board.is_game_over():
        print_board(board)
        
        # Human's turn
        move = None
        while move not in board.legal_moves:
            try:
                move = chess.Move.from_uci(get_human_move()) # type: ignore
                if move not in board.legal_moves:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input format. Please enter a valid move in UCI format.")

        board.push(move)

        if board.is_checkmate():
            print(f"Checkmate! {player_name} wins!")
            human_score += 1
            break
        elif board.is_stalemate() or board.is_insufficient_material():
            print("It's a draw!")
            break

        # Computer's turn
        move = get_computer_move(board)
        print(f"Computer plays: {move}")
        board.push(move)

        if board.is_checkmate():
            print("Checkmate! Computer wins!")
            computer_score += 1
            break
        elif board.is_stalemate() or board.is_insufficient_material():
            print("It's a draw!")
            break

    print(f"Final Score - {player_name}: {human_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()