# Охотник за сокровищами

import random as rd
import sys
import math


def get_new_board():
    # Создать новую структуру данных игрового поля размером 60х15
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if rd.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board


def draw_board(board):
    tens_digits_line = ' '
    for i in range(1, 6):
        tens_digits_line += (' ' * 9) + str(i)

    print(tens_digits_line)
    print(' ' + ('0123456789' * 6))
    print()

    for row in range(15):
        if row < 10:
            extra_space = ' '
        else:
            extra_space = ''

        board_row = ''
        for column in range(60):
            board_row += board[column][row]

        print('%s%s %s %s' % (extra_space, row, board_row, row))
    print(' ' + ('0123456789' * 6))
    print(tens_digits_line)


def get_random_chests(num_chests):
    chests = []
    while len(chests) < num_chests:
        new_chest = [rd.randint(0, 59), rd.randint(0, 14)]
        if new_chest not in chests:
            chests.append(new_chest)
    return chests


def is_on_board(x, y):
    return 0 <= x <= 59 and 0 <= y <= 14


def make_move(board, chests, x, y):
    """Изменить структуру данных поля, используя символ гидролакатора. Удалить сундуки
    с сокровищами из списка с сундуками, как только их нашли. Вернуть False, если это
    не допустимый ход. В противном случае, вернуть строку с рузультатом этого хода."""
    smallest_distance = 100  # Все сундуки будут расположены ближе, чем на расстоянии в 100 единиц.
    for cx, cy in chests:
        distance = math.sqrt((cx - x) ** 2 + (cy - y) ** 2)
        if distance < smallest_distance:
            smallest_distance = distance
        smallest_distance = round(smallest_distance)

        if smallest_distance == 0:
            chests.remove([x, y])
            return 'Вы нашли сундук с сокровищами на затонувшем судне!'
        else:
            if smallest_distance < 10:
                board[x][y] = str(smallest_distance)
                return 'Сундук с сокровищами обнаружен на рассотянии %s от гидролоккатора.' % smallest_distance
            else:
                board[x][y] = 'X'
    return 'Гидролокатор ничего не обнаружил. Все сундуки с сокровищми вне пределов досягаемости.'


def enter_player_move(previous_moves):
    print('Где следует опустить гидролокатор? (координаты: 0-59 0-14) (или введите "выход")')
    while True:
        move = input()
        if move.lower() == 'выход':
            print('Спасибо за игру!')
            sys.exit()
        move = move.split()

        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and is_on_board(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previous_moves:
                print('Здесь вы уже опускали гидролокатор.')
                continue
            return [int(move[0]), int(move[1])]
    print('Введите число от 0 до 59, потом пробел, а затем число от 0 до 14.')


def show_instructions():
    print('''Инструктаж:
Вы - капитан корабля, плывущего за сокровищами. Ваша задача - с помощью
гидролокаторов найти три сундука с сокровищами в затонувших судах на дне океана.
Но гидролокаторы очень просты и определяют только расстояние, но не направление.
Введите координаты, чтобы опустить гидролокатор в воду. На карте будет показано
число, обозначающее, на каком расстоянии находится ближайший сундук. Или будет
показана буква Х, обозначающая, что сундук в области действия гидролокатора не
обнаружен. На карте ниже метки C - это сундуки.
Цифра 3 обозначает, что ближайший сундук находится на отдалении в 3 единицы.

                                1         2         3
                      012345678901234567890123456789012
                    0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
                    1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
                    2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
                    3 ````````~~~`````~~~`~`````~`~``~` 3
                    4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4
                      012345678901234567890123456789012
                                1         2         3
(Во время игры сундуки на карте не обозначаются!)

Нажмите клавишу Enter, чтобы продолжить...''')

    input()

    print('''Если гидролокатор опущен прямо на сундук, вы сможете поднять
сундук. Другие гидролокаторы обновят данные о расположении ближайшего сундука.
Сундуки ниже находятся вне диапазона локатора, поэтому отображается буква X.


                                1         2         3
                      012345678901234567890123456789012
                    0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
                    1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
                    2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
                    3 ````````~~~`````~~~`~`````~`~``~` 3
                    4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4
                      012345678901234567890123456789012
                                1         2         3

Сундуки с сокровищами не перемещаются. Гидролокаторы определяют сундуки
на расстоянии до 9 единиц. Попробуйте поднять все 3 сундука до того, как все
гидролокаторы будут опущены на дно. Удачи!

Нажмите клавишу Enter, чтобы продолжить...''')
    input()


print('Охотник за сокровищами!')
print()
print('Показать инструктаж? (да/нет)')
if input().lower().startswith('д'):
    show_instructions()

while True:
    sonar_devices = 20
    the_board = get_new_board()
    the_chests = get_random_chests(3)
    draw_board(the_board)
    previous_moves = []

    while sonar_devices > 0:
        print('Осталось гидролокаторов: %s. Осталось сундуков с сокровищами: %s' % (sonar_devices, len(the_chests)))
        x, y = enter_player_move(previous_moves)
        previous_moves.append((x, y))
        move_result = make_move(the_board, the_chests, x, y)
        if not move_result:
            continue
        else:
            if move_result == 'Вы нашли сундук с сокровищами на затонувшем судне!':
                for x, y in previous_moves:
                    make_move(the_board, the_chests, x, y)
            draw_board(the_board)
            print(move_result)

        if len(the_chests) == 0:
            print('Вы нашли все сундуки с сокровищами на затонувших суднах! Поздравляем и приятной игры!')
            break

        sonar_devices -= 1
    if sonar_devices == 0:
        print('Все гидролокаторы опущены на дно! Придется разворачивать корабль и')
        print('отправляться домой, в порт! Игра окончена.')
        print('Вы не нашли сундуки в следующих местах:')
        for x, y in the_chests:
            print(' %s, %s' % x, y)

    print('Хотите сыграть ещё раз? (да или нет)')
    if not input().lower().startswith('д'):
        sys.exit()
