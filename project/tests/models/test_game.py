from src.models.game import Game
from src.models.player import Player
from src.models.square import Square
from src.models.move import MoveMaker
# from src.services.play_game import StartGame

def test_has_two_players():
    player1_name = "Allan"
    player2_name = "Franklin"
    player1 = Player('X', player1_name)
    player2 = Player('O', player2_name)
    assert player1.__dict__ == {'symbol': 'X', 'name': "Allan"}
    assert player2.__dict__ == {'symbol': 'O', 'name': "Franklin"}

def test_square():
    square_test = Square()
    assert square_test.__dict__['board'] == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def test_move_maker():
    square = Square()
    player1_name = "Allan"
    player2_name = "Franklin"
    player1 = Player('X', player1_name)
    player2 = Player('O', player2_name)
    move_maker = MoveMaker(square)
    assert move_maker.display_board_test() == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    move1 = move_maker.make_move(5, player1)
    assert move_maker.display_board_test() == [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
    move2 = move_maker.make_move(1, player2)
    assert move_maker.display_board_test() == [['O', 2, 3], [4, 'X', 6], [7, 8, 9]]
    move3 = move_maker.make_move(4, player1)
    assert move_maker.display_board_test() == [['O', 2, 3], ['X', 'X', 6], [7, 8, 9]]
    move4 = move_maker.make_move(6, player1)
    assert move_maker.display_board_test() == [['O', 2, 3], ['X', 'X', 'X'], [7, 8, 9]]
    
def test_winner():
    square = Square()
    game = Game(square)
    player1_name = "Allan"
    player2_name = "Franklin"
    player1 = Player('X', player1_name)
    player2 = Player('O', player2_name)
    move_maker = MoveMaker(square)
    move_maker.make_move(5, player1)
    move_maker.make_move(1, player2)
    move_maker.make_move(4, player1)
    move_maker.make_move(6, player1)
    assert game.check_for_winner() == "Winner: X"
