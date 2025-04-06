class Board:
    def __init__(self):
        self.pieces = Board.__init_board()

    def __init_board():
        board = [[''] * 8 for _ in range(3)] + \
                [['', '', '', 'b', 'w', '', '', '']] + \
                [['', '', '', 'w', 'b', '', '', '']] + \
                [[''] * 8 for _ in range(3)]
        return board

    def can_place_piece(self, piece):
        if piece not in ('b', 'w'):
            return False

        for x in range(8):
            for y in range(8):
                if self.pieces[y][x] == '':
                    if self.__reverse(piece, x, y, False):
                        return True
        return False

    def get_winner(self):
        w_count = sum(row.count('w') for row in self.pieces)
        b_count = sum(row.count('b') for row in self.pieces)
        if (w_count > b_count):
            return 'w'
        elif (b_count > w_count):
            return 'b'
        else:
            return ''

    def place_piece(self, piece, x_pos, y_pos):
        if self.pieces[y_pos][x_pos] != '':
            raise ValueError('Pieces must be placed on empty squares')

        reverse_performed = self.__reverse(piece, x_pos, y_pos, True)

        if not reverse_performed:
            raise ValueError('Move must reverse at least one opponents piece')

        self.pieces[y_pos][x_pos] = piece

    def __reverse(self, piece, x_pos, y_pos, do_reverse):
        positions = []
        positions.append(zip(range(x_pos + 1, 8), [y_pos] * (8 - x_pos)))
        positions.append(zip(range(x_pos - 1, -1, -1), [y_pos] * (x_pos + 1)))
        positions.append(zip([x_pos] * (8 - y_pos), range(y_pos + 1, 8)))
        positions.append(zip([x_pos] * (y_pos + 1), range(y_pos - 1, -1, -1)))

        diag_1_min = min(8 - x_pos, y_pos + 1)
        positions.append(zip(range(x_pos + 1, x_pos + diag_1_min),
                         range(y_pos - 1, y_pos - diag_1_min, -1)))
        diag_2_min = min(x_pos + 1, y_pos + 1)
        positions.append(zip(range(x_pos - 1, x_pos - diag_2_min, -1),
                         range(y_pos - 1, y_pos - diag_2_min, -1)))
        diag_3_min = min(x_pos + 1, 8 - y_pos)
        positions.append(zip(range(x_pos - 1, x_pos - diag_3_min, -1),
                         range(y_pos + 1, y_pos + diag_3_min)))
        diag_4_min = min(8 - x_pos, 8 - y_pos)
        positions.append(zip(range(x_pos + 1, x_pos + diag_4_min),
                         range(y_pos + 1, y_pos + diag_4_min)))

        reverse_performed = False
        for position in positions:
            reverse_performed |= self.__reverse_dimension(
                piece, list(position), do_reverse)
        return reverse_performed

    def __reverse_dimension(self, piece, positions, do_reverse):
        if not self.__dimension_has_second_piece(piece, positions):
            return False

        reverse_performed = False
        for x, y in positions:
            if self.pieces[y][x] == piece:
                break
            reverse_performed = True
            if do_reverse:
                self.pieces[y][x] = piece

        return reverse_performed

    def __dimension_has_second_piece(self, piece, positions):
        for x, y in positions:
            if self.pieces[y][x] == '':
                return False
            if self.pieces[y][x] == piece:
                return True
        return False
