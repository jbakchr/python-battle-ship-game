class Cell():
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column
        self.is_picked = False
        self.contains_ship = False

    def get_is_picked(self):
        return self.is_picked

    def set_is_picked(self):
        self.is_picked = True

    def get_contains_ship(self):
        return self.contains_ship
