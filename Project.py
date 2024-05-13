import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9

    def print_board(self):
        for i in range(0, 9, 3):
            print('|'.join(self.board[i:i + 3]))

    def check_winner(self, player):
        # Check rows
        for i in range(0, 9, 3):
            if all(cell == player for cell in self.board[i:i + 3]):
                return True

        # Check columns
        for i in range(3):
            if all(cell == player for cell in self.board[i::3]):
                return True

        # Check diagonals
        if all(cell == player for cell in self.board[::4]) or all(cell == player for cell in self.board[2:8:2]):
            return True

        return False

    def is_board_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.check_winner('X') or self.check_winner('O') or self.is_board_full()

    def get_empty_cells(self):
        return [index for index, value in enumerate(self.board) if value == ' ']

    def minimax(self, maximizing_player):
        if self.check_winner('X'):
            return -1
        elif self.check_winner('O'):
            return 1
        elif self.is_board_full():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.get_empty_cells():
                self.board[move] = 'O'
                eval_score = self.minimax(False)
                self.board[move] = ' '
                max_eval = max(max_eval, eval_score)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_empty_cells():
                self.board[move] = 'X'
                eval_score = self.minimax(True)
                self.board[move] = ' '
                min_eval = min(min_eval, eval_score)
            return min_eval

    def find_best_move(self):
        best_val = float('-inf')
        best_move = -1

        for move in self.get_empty_cells():
            self.board[move] = 'O'
            move_val = self.minimax(False)
            self.board[move] = ' '

            if move_val > best_val:
                best_move = move
                best_val = move_val

        return best_move


def player_move(game):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and game.board[move] == ' ':
                game.board[move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def computer_move(game):
    print("Computer is thinking...")
    move = game.find_best_move()
    game.board[move] = 'O'


def main():
    game = TicTacToe()

    while True:
        player_choice = input("Do you want to begin? (Yes/No): ").lower()
        if player_choice in ('yes', 'no'):
            break
        else:
            print("Invalid choice. Please enter 'Yes' or 'No'.")

    if player_choice == 'no':
        computer_move(game)

    while not game.is_game_over():
        game.print_board()
        player_move(game)

        if game.is_game_over():
            break

        game.print_board()
        computer_move(game)

    game.print_board()

    if game.check_winner('X'):
        print("Congratulations! You win!")
    elif game.check_winner('O'):
        print("Computer wins. Better luck next time.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
