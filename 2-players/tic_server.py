"""Creates a server and accepts connection to play tic tac toe"""
import socket
import time

import tic_functions as tf
from game_settings import Settings


class Server:
    """A class to create a server for tic-tac-toe"""

    def __init__(self, host: str, port: int):
        """Initiate the server with host and port and create the clients dict"""
        self.host = host
        self.port = port
        self.clients = dict()
        self.server = self.create_server()
        self.settings = Settings()
        self.active_player = self.settings.active_player

    def create_server(self):
        """Create the server, binds it and start listening"""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen()
        return server

    def broadcast(self, message):
        """Send messages to all clients"""
        for player in self.settings.players:
            player.client.send(f'{message}'.encode('utf-8'))

    def broadcast_board(self, board):
        """Send board game to all clients"""
        for player in self.settings.players:
            player.client.send(board.encode('utf-8'))

    def broadcast_move(self, move, active_player):
        """Send move to other player"""
        for player in self.settings.players:
            if player == active_player:
                continue
            player.client.send(f'{active_player.name} played {move}'.encode('utf-8'))

    def receive(self):
        """Accept new connection for each client"""
        while True:
            # Accept new connection
            client, add = self.server.accept()

            # Request, print nickname and add it to clients
            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            print(f'The nickname is {nickname}')
            self.clients[client] = nickname

            # Notify the client he is connected and notify others
            client.send('Connected to server'.encode('utf-8'))
            for user in self.clients:
                if user == client:
                    continue
                user.send(f'{self.clients[client]} joined!'.encode('utf-8'))

            # Check for 2 clients to start game
            if len(self.clients) < 2:
                client.send('\nWaiting for player.'.encode('utf-8'))

            else:
                self.player_assignment()

    def player_assignment(self):
        """Assign clients to player 1 and 2"""
        player1, player2 = self.game_start(self.clients.copy())
        self.settings.players.append(player1)
        self.settings.players.append(player2)
        self.broadcast(f'{self.settings.players[0].nickname} is {self.settings.players[0].name}\n'
                       f'{self.settings.players[1].nickname} is {self.settings.players[1].name}')
        player1.client.send('\nYour symbol is x'.encode('utf-8'))
        player2.client.send('\nYour symbol is o'.encode('utf-8'))
        time.sleep(1.0)
        self.tic_game()

    def game_start(self, clients):
        """Initiate players, file and board game"""
        player1, player2 = tf.start_game(clients)
        self.settings.game_active = True
        self.active_player = player1
        return player1, player2

    def tic_game(self):
        """Start the game main function"""
        # Send player request for input
        self.broadcast(f'{self.active_player.name} turn')

        # get player input
        move = tf.validate_input(self.active_player.client, self.settings.board)
        print(f'{self.active_player.nickname} wrote: {move}')
        self.broadcast_move(move, self.active_player)

        # Add symbol to board game
        self.settings.board[move] = self.active_player.symbol
        time.sleep(0.5)

        # Concatenate board game and send to players
        board_state = tf.show_board(self.settings.board)
        self.broadcast_board(board_state)

        # Check for win or draw
        result, self.settings.game_active = tf.check_win(self.settings.game_active,
                                                         self.settings.board)
        if result:
            self.broadcast(f'{self.active_player.name} won\n')
            print(f'{self.active_player.nickname} won')

        message, self.settings.game_active = tf.check_draw(self.settings.game_active,
                                                           self.settings.board)
        if len(message) != 0:
            self.broadcast(message)

        if self.settings.game_active:
            self.active_player = tf.switch_player(self.settings.players.copy(), self.active_player)
            return self.tic_game()
        else:
            self.broadcast('Would you like to play again? (y/n)')
            message1 = self.settings.players[0].client.recv(1024).decode('utf-8')
            message2 = self.settings.players[1].client.recv(1024).decode('utf-8')
            if message1.lower() == message2.lower() == 'y':
                self.settings = Settings()
                self.player_assignment()
            else:
                self.broadcast('Thank you for playing')


if __name__ == '__main__':
    tic_server = Server('127.0.0.1', 55555)
    tic_server.receive()
