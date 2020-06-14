import random as rd


def draw_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def input_player_letter():
    letter = ''
    while not letter == 'Х' or letter == 'О':
        print('Вы выбираете X или O?')
        letter = input().upper()

    if letter == 'Х':
        return ['Х', 'О']
    else:
        return ['О', 'Х']


def who_goes_first():
    if rd.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'


def make_move(board, letter, move):
    board[move] = letter


def is_winner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or  # через верх
            (board[4] == letter and board[5] == letter and board[6] == letter) or  # через ценрт
            (board[1] == letter and board[2] == letter and board[3] == letter) or  # через низ
            (board[7] == letter and board[4] == letter and board[1] == letter) or  # вниз по левой стророне
            (board[8] == letter and board[5] == letter and board[2] == letter) or  # вниз по центру
            (board[9] == letter and board[6] == letter and board[3] == letter) or  # вниз по рпавой стороне
            (board[7] == letter and board[5] == letter and board[3] == letter) or  # по диагонали
            (board[9] == letter and board[5] == letter and board[1] == letter))  # по диагонали


def get_board_copy(board):
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def is_space_free(board, move):
    return board[move] == ' '


def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('Ваш следующий ход? (1-9)')
        move = input()
    return int(move)


def choose_random_move_from_list(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return rd.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    if computer_letter == 'Х':
        player_letter = 'О'
    else:
        player_letter = 'Х'

    # Сначала проверка - подедит ли компьютер сделав следующий ход
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, computer_letter, i)
            if is_winner(board_copy, computer_letter):
                return i

    # Проверка - победит ди игрок, сделав следующий ход, компьютер блокирует его
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, player_letter, i)
            if is_winner(board_copy, player_letter):
                return i

    # Компьтер пробует занять один из углов, если они свободные
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Компьютер пробует занять центр, если он свободен
    if is_space_free(board, 5):
        return 5

    # Компьютер делает ход по одной строне
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print('Игра "Крестики-нолики"')

while True:
    # Перезагрузка игрового поля
    the_board = [' '] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print('' + turn + ' ходит первым.')
    game_is_playing = True
    while game_is_playing:
        if turn == 'Человек':
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('Ура! Вы выйграли!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('Ничья!')
                    break
                else:
                    turn = 'Компьютер'
        else:
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print('Компьютер победил! Вы проиграли.')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('Ничья!')
                    break
                else:
                    turn = 'Человек'

    print('Сыграем ещё раз? (да или нет)')
    if not input().lower().startswith('д'):
        break
