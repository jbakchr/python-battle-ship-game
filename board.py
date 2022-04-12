from random import shuffle, randint
from ship import Ship
from cell import Cell


class Board():
    def __init__(self) -> None:
        self.create_board()
        self.create_ships()
        self.set_ships_on_board()

    def create_board(self):
        board = []
        for i in range(0, 10):
            row = []
            for j in range(0, 10):
                cell = Cell(i, j)
                row.append((cell))
            board.append(row)
        self.board = board

    def create_ships(self):
        ship_lengths = [2, 3, 3, 4, 5]
        ships = []

        for length in ship_lengths:
            ship = Ship(length)
            ships.append(ship)

        shuffle(ships)
        self.ships = ships

    def set_ships_on_board(self):
        for ship in self.ships:
            while not ship.is_set_on_board():
                direction = randint(0, 1)
                if direction:
                    print("Set ship horizontal")
                else:
                    self.set_ship_vertically(ship)
                break

    def set_ship_vertically(self, ship):
        # Generate random row and column for ship to be set on
        row = randint(0, self.get_width_of_board() - ship.get_ship_length())
        column = randint(0, self.get_width_of_board() - 1)

        # Check if ship can be set from position and downwards
        can_ship_be_set = False
        while not can_ship_be_set:
            counter = 0
            for index in range(row, row + ship.get_ship_length()):
                # Check if cell contains ship
                cell = self.get_board_cell(index, column)
                if not cell.get_contains_ship():
                    counter += 1

            if counter == ship.get_ship_length():
                can_ship_be_set = True
            else:
                row = randint(0, self.get_width_of_board() -
                              ship.get_ship_length())
                column = randint(0, self.get_width_of_board() - 1)

        # Set ship
        for index in range(row, row + ship.get_ship_length()):
            cell = self.get_board_cell(index, column)
            cell.set_contains_ship()

    def get_board(self):
        return self.board

    def get_width_of_board(self):
        return len(self.board[0])

    def print_board(self):
        self.print_top_of_board()
        self.print_board_cells()
        print()

    def print_top_of_board(self):
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

    def get_board_cell(self, row, column):
        return self.get_board()[row][column]

    def set_board_cell(self, row, column):
        cell = self.get_board()[row][column]
        cell.set_is_picked()
