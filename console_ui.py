TOP_BAR = '   ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗\n'
SEPARATOR = '\n   ╟───┼───┼───┼───┼───┼───┼───┼───╢\n'
BOTTOM_BAR = '\n   ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝\n'
LETTERS = '     A   B   C   D   E   F   G   H\n'
CLEAR = '\033[H\033[2J'


class ConsoleUI:
    def __piece_char(piece):
        if piece == 'b':
            return '●'
        elif piece == 'w':
            return '○'
        return ' '

    def input_move(self):
        while True:
            move = input("> ")
            # TODO validate input
            x = ord(move[0].lower()) - 97
            y = int(move[1]) - 1
            return (x, y)

    def output_message(self, message):
        print(message)

    def output_game_state(self, game, color):
        print(CLEAR)
        row_strs = []
        for i in range(len(game.board.pieces)):
            row = game.board.pieces[i]
            piece_strs = [ConsoleUI.__piece_char(p) for p in row]
            row_strs.append(f' {i + 1} ║ {" │ ".join(piece_strs)} ║ {i + 1}')

        board = LETTERS + TOP_BAR + \
            SEPARATOR.join(row_strs) + BOTTOM_BAR + LETTERS
        print(board)

        print(f'Your Color: {ConsoleUI.__piece_char(color)}')
        if (game.current_player == color):
            print('It is your turn.')
        elif (game.current_player != ''):
            print('It is your opponents turn.')
        else:
            print('The game is over.')
