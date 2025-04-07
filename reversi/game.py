import board


class Game:
    def __init__(self):
        self.board = board.Board()
        self.current_player = 'b'
        self.player_has_passed = False

    def make_move(self, x_pos, y_pos):
        self.board.place_piece(self.current_player, x_pos, y_pos)

        if not self.player_has_passed:
            self.__switch_player()

        if not self.board.can_place_piece(self.current_player):
            self.player_has_passed = True
            self.__switch_player()

            if not self.board.can_place_piece(self.current_player):
                self.current_player = ''

    def __switch_player(self):
        if self.current_player == 'b':
            self.current_player = 'w'
        elif self.current_player == 'w':
            self.current_player = 'b'
