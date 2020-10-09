class Settings:
    """A class to keep track of the game state"""
    def __init__(self):
        self.board = {key: ' ' for key in map(str, range(1, 10))}
        self.game_active = False
        self.players = list()
        self.active_player = None
