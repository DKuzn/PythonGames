import random as rd
import time


def display_info():
    print('''Вы находитесь в землях, заселенных драконами.
Перед собой вы видите две пещеры. В одной их них - дружелюбный дракон,
который готов поделиться с вами своими сокровищами. Во второй - 
жадный и голодный дракон, который вас съест.''')


def choose_cave():
    time.sleep(1)
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру войдете? (нажмите клавишу 1 или 2)')
        cave = input()
    return cave


def check_cave(chosen_cave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    time.sleep(2)

    friendly_cave = rd.randint(1, 2)

    if chosen_cave == str(friendly_cave):
        print('...делится сокровищами!')
    else:
        print('...моментально съедает вас!')


playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    display_info()
    caveNumber = choose_cave()
    check_cave(caveNumber)

    print('Попытаете удачу ещё раз? (да или нет)')
    playAgain = input()
