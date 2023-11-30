from src.models.game import Game
from src.models.square import Square
from src.models.move import MoveMaker
from src.services.play_game import StartGame

def main():

    player1_name = input("Enter name for Player 1 (X): ")
    player2_name = input("Enter name for Player 2 (O): ")

    square = Square()
    move_maker = MoveMaker(square)
    game = Game(square)

    tictactoe_game = StartGame(player1_name, player2_name)
    tictactoe_game.start_game(square, move_maker, game)


if __name__ == "__main__":
    main()