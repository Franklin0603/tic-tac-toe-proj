class MoveMaker:
    def __init__(self, square) -> None:
        self.position = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 9: (2, 2)
        }
        self.square = square

    def display_board(self):
        for row in self.square.board:
            print(row)

    def display_board_test(self):
        return self.square.board

    def make_move(self, spot, player):
        if spot in self.position:
            row, col = self.position[spot]
            if self.square.board[row][col] not in ['X', 'O']:
                self.square.board[row][col] = player.symbol
                print("Great move! Now it's the next player's turn")
                return True 
            else:
                print("That spot is taken, please choose one with a number available")
                return False
        else:
            print("Invalid spot number.")
            return False 