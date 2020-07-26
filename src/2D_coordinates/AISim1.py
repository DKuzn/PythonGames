# "Реверси": клон "Отелло".
"""ИИ из файла reverse.py играет сам с собой.
Игроку выводится финальная доска и предлагется выйти или сыграть ещё раз."""
import random as rd

WIDTH = 8
HEIGHT = 8


def draw_board(board):
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y + 1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y + 1))
    print(' +--------+')
    print('  12345678')


def get_new_board():
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board


def is_valid_move(board, tile, xstart, ystart):
    # Вернуть False, если ход игрока в клетку с координатами xstart, ystart - недопустимый.
    # Если это допустимый ход, вернуть список клеток, которые "присвоил" бы игрок, если бы сделал туда ход.
    if board[xstart][ystart] != ' ' or not is_on_board(xstart, ystart):
        return False

    if tile == 'Х':
        other_tile = 'О'
    else:
        other_tile = 'Х'

    tiles_to_flip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while is_on_board(x, y) and board[x][y] == other_tile:
            x += xdirection
            y += ydirection
            if is_on_board(x, y) and board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tiles_to_flip.append([x, y])

    if len(tiles_to_flip) == 0:
        return False
    return tiles_to_flip


def is_on_board(x, y):
    return 0 <= x <= WIDTH - 1 and 0 <= y <= HEIGHT - 1


def get_board_with_valid_moves(board, tile):
    board_copy = get_board_copy(board)

    for x, y in get_valid_moves(board_copy, tile):
        board_copy[x][y] = '.'
    return board_copy


def get_valid_moves(board, tile):
    valid_moves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if is_valid_move(board, tile, x, y):
                valid_moves.append([x, y])
    return valid_moves


def get_score_of_board(board):
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'Х':
                xscore += 1
            if board[x][y] == 'О':
                oscore += 1
    return {'Х': xscore, 'О': oscore}


def enter_player_tile():
    tile = ''
    while not (tile == 'Х' or tile == 'О'):
        print('Вы играете за Х или О?')
        tile = input().upper()

    if tile == 'Х':
        return ['Х', 'О']
    else:
        return ['О', 'Х']


def who_goes_first():
    if rd.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'


def make_move(board, tile, xstart, ystart):
    tiles_to_flip = is_valid_move(board, tile, xstart, ystart)

    if not tiles_to_flip:
        return False

    board[xstart][ystart] = tile
    for x, y in tiles_to_flip:
        board[x][y] = tile
    return True


def get_board_copy(board):
    board_copy = get_new_board()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            board_copy[x][y] = board[x][y]

    return board_copy


def is_on_corner(x, y):
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)


def get_computer_move(board, computer_tile):
    possible_moves = get_valid_moves(board, computer_tile)
    rd.shuffle(possible_moves)

    for x, y in possible_moves:
        if is_on_corner(x, y):
            return [x, y]

    best_score = -1
    for x, y in possible_moves:
        board_copy = get_board_copy(board)
        make_move(board_copy, computer_tile, x, y)
        score = get_score_of_board(board_copy)[computer_tile]
        if score > best_score:
            best_move = [x, y]
            best_score = score
    return best_move


def print_score(board, player_tile, computer_tile):
    scores = get_score_of_board(board)
    print('Ваш счет: %s. Счет компьютера: %s.' % (scores[player_tile], scores[computer_tile]))


def play_game(player_tile, computer_tile):
    turn = who_goes_first()
    print(turn + ' ходит первым.')

    board = get_new_board()
    board[3][3] = 'Х'
    board[3][4] = 'О'
    board[4][3] = 'О'
    board[4][4] = 'Х'

    while True:
        player_valid_moves = get_valid_moves(board, player_tile)
        computer_valid_moves = get_valid_moves(board, computer_tile)

        if player_valid_moves == [] and computer_valid_moves == []:
            return board

        elif turn == 'Человек':
            if player_valid_moves:
                move = get_computer_move(board, player_tile)
                make_move(board, player_tile, move[0], move[1])
            turn = 'Компьютер'

        elif turn == 'Компьютер':
            if computer_valid_moves:
                move = get_computer_move(board, computer_tile)
                make_move(board, computer_tile, move[0], move[1])
            turn = 'Человек'


print('Приветствуем в игре "Реверси"!')

player_tile, computer_tile = ['Х', 'О']

while True:
    final_board = play_game(player_tile, computer_tile)

    draw_board(final_board)
    scores = get_score_of_board(final_board)
    print('X набрал %s очков. O набрал %s очков.' % (scores['Х'], scores['О']))
    if scores[player_tile] > scores[computer_tile]:
        print('Вы победили компьютер, обогнав его на %s очков! Поздравления!'
              % (scores[player_tile] - scores[computer_tile]))
    elif scores[player_tile] < scores[computer_tile]:
        print('Вы проиграли. Компьютер победил вас, обогнав на %s очков.'
              % (scores[computer_tile] - scores[player_tile]))
    else:
        print('Ничья!')

    print('Хотите сыграть ещё раз? (да или нет)')
    if not input().lower().startswith('д'):
        break
