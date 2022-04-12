class Board():
    def __init__(self) -> None:
        print("The Board ..")

        # When the Board first initializes it needs to create a 10 x 10
        # board
        self.board = self.create_board()
        print(self.board)

    def create_board(self):
        board = []
        for i in range(0, 10):
            row = []
            for j in range(0, 10):
                row.append((i, j))
            board.append(row)
        return board
