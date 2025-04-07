import re

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
            move = input("> ").strip()

            if not re.match(r'^[a-hA-H][1-8]$', move):
                raise ValueError('Position must be in the format [A-Z][1-8].')

            x = ord(move[0].lower()) - 97
            y = int(move[1]) - 1
            return (x, y)

    def output_message_and_wait(self, message):
        print(message)
        input('Press <return> to continue.')

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
            winner = game.board.get_winner()
            if winner == color:
                print('You won the game.')
            elif winner == '':
                print('It is a draw.')
            else:
                print('You lost the game.')
