from battle_ship_game import BattelShipGame

try:
    game = BattelShipGame()
    game.play()
except KeyboardInterrupt:
    print("\n\nOkay then. Bye bye then .. 👋\n")
