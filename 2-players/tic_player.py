class Player:
    """A class to define players for tic-tac-toe"""
    client = None
    nickname = None

    def __init__(self, symbol, name):
        """Initiate the symbol for the player"""
        self.symbol = symbol
        self.name = name
