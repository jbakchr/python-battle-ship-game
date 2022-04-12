class Ship():
    def __init__(self, ship_length) -> None:
        self.ship_length = ship_length
        self.sat_on_board = False

    def get_ship_length(self):
        return self.ship_length

    def is_set_on_board(self):
        return self.sat_on_board
