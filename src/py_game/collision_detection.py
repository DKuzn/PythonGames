import pygame
import sys
import random as rd
from pygame.locals import *

pygame.init()
main_clock = pygame.time.Clock()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Обнаружение столкновений')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Создание структур данных игрока и "еды".
food_counter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(rd.randint(0, WINDOWWIDTH - FOODSIZE),
                             rd.randint(0, WINDOWHEIGHT - FOODSIZE),
                             FOODSIZE, FOODSIZE))


# Создание переменных перемещения
move_left = False
move_right = False
move_up = False
move_down = False

MOVESPEED = 6


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Изменение переменных клавиатуры
            if event.key == K_LEFT or event.key == K_a:
                move_right = False
                move_left = True
            if event.key == K_RIGHT or event.key == K_d:
                move_left = False
                move_right = True
            if event.key == K_UP or event.key == K_w:
                move_down = False
                move_up = True
            if event.key == K_DOWN or event.key == K_s:
                move_up = False
                move_down = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                move_left = False
            if event.key == K_RIGHT or event.key == K_d:
                move_right = False
            if event.key == K_UP or event.key == K_w:
                move_up = False
            if event.key == K_DOWN or event.key == K_s:
                move_down = False
            if event.key == K_x:
                player.top = rd.randint(0, WINDOWHEIGHT - player.height)
                player.left = rd.randint(0, WINDOWWIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    food_counter += 1
    if food_counter >= NEWFOOD:
        # Добавление "еды".
        food_counter = 0
        foods.append(pygame.Rect(rd.randint(0, WINDOWWIDTH - FOODSIZE),
                                 rd.randint(0, WINDOWHEIGHT - FOODSIZE),
                                 FOODSIZE, FOODSIZE))

    window_surface.fill(WHITE)

    # Перемещение игрока
    if move_down and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if move_up and player.top > 0:
        player.top -= MOVESPEED
    if move_left and player.left > 0:
        player.left -= MOVESPEED
    if move_right and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # Отображение игрока на поверхности
    pygame.draw.rect(window_surface, BLACK, player)

    # Проверка, не пересекся ли игрок с какими-либо блоками "еды"
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    # Отображение "еды".
    for i in range(len(foods)):
        pygame.draw.rect(window_surface, GREEN, foods[i])

    pygame.display.update()
    main_clock.tick(40)
