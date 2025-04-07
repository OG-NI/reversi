import socket
import random
import json

import game
import console_ui

BUFSIZE = 1024


class SocketConnection:
    # TODO change to abstract subclass "UI"
    def __init__(self, ui: console_ui.ConsoleUI):
        self.socket = socket.socket()
        self.game = game.Game()
        self.connection = None
        self.color = None
        self.ui = ui

    def __del__(self):
        self.socket.close()

    def host(self, port):
        self.socket.bind(('', port))
        self.socket.listen(0)
        self.connection, _ = self.socket.accept()

        # randomly assign player piece colors
        colors = ['b', 'w']
        self.color = random.choice(colors)
        colors.remove(self.color)
        self.connection.send(colors[0].encode())

        self.start()

    def join(self, ip, port):
        self.socket.connect((ip, port))
        self.connection = self.socket
        self.color = self.connection.recv(BUFSIZE).decode()
        self.start()

    def start(self):
        while True:
            self.ui.output_game_state(self.game, self.color)

            if self.game.current_player == '':
                break
            elif self.game.current_player == self.color:
                try:
                    x, y = self.ui.input_move()
                    self.game.make_move(x, y)
                    self.connection.send(json.dumps((x, y)).encode())
                except ValueError as error:
                    self.ui.output_message_and_wait(str(error))
            else:
                x, y = json.loads(self.connection.recv(BUFSIZE).decode())
                try:
                    self.game.make_move(x, y)
                except ValueError:
                    pass  # ignore invalid moves made by opponent

    # TODO send and receive in separate functions
