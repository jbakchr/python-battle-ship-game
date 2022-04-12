class GameHeader():
    def __init__(self, title) -> None:
        self.title = "!! " + title + " !!"

    def print_game_header(self):
        print("*" * len(self.title))
        print(self.title)
        print("*" * len(self.title))
