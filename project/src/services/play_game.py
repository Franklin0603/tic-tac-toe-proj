from src.models.player import Player

class StartGame:
    def __init__(self, player1_name, player2_name) -> None:
        self.player1 = Player('X', player1_name)
        self.player2 = Player('O', player2_name)

    def start_game(self, square, move_maker, game):
        for turn in range(9):
            move_maker.display_board()
            player = self.player1 if turn % 2 == 0 else self.player2

            # Get player input and make move
            try:
                spot = int(input(f"{player.name} ({player.symbol}'s turn). Enter a spot (1-9): "))
                if 1 <= spot <= 9:
                    move_maker.make_move(spot, player)
                else:
                    print("Please enter a number between 1 and 9.")
            except ValueError:
                print("Please enter a valid number.")

            # Check for winner
            winner = game.check_for_winner()
            if winner != 'No winner':
                print(winner)
                #move_maker.display_board()
                break
        else:
            print("The game ended in a draw.")
            move_maker.display_board()