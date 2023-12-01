class Game:
    def __init__(self, square):
        self.square = square
        self.winner_condition = None

    def check_for_winner(self):
        board = self.square.board

        # Check rows
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] and isinstance(board[row][0], str):
                self.winner_condition = ['row', row]
                return f"Winner: {board[row][0]}; Winner condition: {self.winner_condition}"

        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and isinstance(board[0][col], str):
                self.winner_condition = ['row', row]
                return f"Winner: {board[0][col]}; Winner condition: {self.winner_condition}"
                return f'Winner: {board[0][col]}'

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and isinstance(board[0][0], str):
            return f'Winner: {board[0][0]}'
        if board[0][2] == board[1][1] == board[2][0] and isinstance(board[0][2], str):
            return f'Winner: {board[0][2]}'

        return 'No winner'