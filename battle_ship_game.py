from board import Board


class BattelShipGame():
    def __init__(self) -> None:
        self.is_game_over = False
        self.game_board = Board()

    def play(self):
        while not self.is_game_over:
            self.game_board.print_board()
            (row, column) = self.ask_user_to_pick_cell()
            self.game_board.set_board_cell(int(row), int(column))

    def ask_user_to_pick_cell(self):
        print("Please choose row and column")
        row = input("Row (0-9): ")
        column = input("Column (0-9): ")
        return (row, column)
