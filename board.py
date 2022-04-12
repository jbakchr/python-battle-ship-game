from cell import Cell


class Board():
    def __init__(self) -> None:
        self.create_board()

    def create_board(self):
        board = []
        for i in range(0, 10):
            row = []
            for j in range(0, 10):
                cell = Cell(i, j)
                row.append((cell))
            board.append(row)
        self.board = board

    def get_board(self):
        return self.board

    def get_width_of_board(self):
        return len(self.board[0])

    def print_board(self):
        self.print_divider()
        self.print_board_cells()

    def print_divider(self):
        top_to_print = " "
        for i in range(0, self.get_width_of_board()):
            top_to_print += "_ "
        print(top_to_print)

    def print_board_cells(self):
        for row in self.get_board():
            row_to_print = "|"
            for cell in row:
                if cell.get_is_picked():
                    if cell.get_contains_ship():
                        row_to_print += "\033[4mx\033[0m" + "|"
                    else:
                        row_to_print += "\033[4mo\033[0m" + "|"
                else:
                    row_to_print += "_|"
            print(row_to_print)
