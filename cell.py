class Cell():
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column
        self.is_picked = False
        self.contains_ship = False
