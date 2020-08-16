import pygame
import random
import sys
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 40
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5


def terminate():
    pygame.quit()
    sys.exit()


def wait_for_player_to_press_key():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return


def player_has_hit_baddie(player_rect, baddies):
    for b in baddies:
        if player_rect.colliderect(b['rect']):
            return True
    return False


def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


pygame.init()
main_clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Ловкач')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 35)

game_over_sound = pygame.mixer.Sound('data/gameover.wav')
pygame.mixer.music.load('data/background.mid')

player_image = pygame.image.load('data/player.png')
player_rect = player_image.get_rect()
baddie_image = pygame.image.load('data/baddie.png')

# Вывод начального экрана.
window_surface.fill(BACKGROUNDCOLOR)
draw_text('Ловкач', font, window_surface, (WINDOWWIDTH // 3), (WINDOWHEIGHT // 3))
draw_text('Нажмите клавишу для начала игры.', font, window_surface, (WINDOWWIDTH // 5) - 50, (WINDOWHEIGHT // 3) + 50)
pygame.display.update()
wait_for_player_to_press_key()

top_score = 0
while True:
    # Настройка начала игры.
    baddies = []
    score = 0
    player_rect.topleft = (WINDOWWIDTH // 2, WINDOWHEIGHT - 50)
    move_left = move_right = move_up = move_down = False
    reverse_cheat = slow_cheat = False
    baddie_add_counter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True:  # Игровой цикл выполняется пока игра работает.
        score += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverse_cheat = True
                if event.key == K_x:
                    slow_cheat = True
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
                if event.key == K_z:
                    reverse_cheat = False
                    score = 0
                if event.key == K_x:
                    slow_cheat = False
                    score = 0
                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or event.key == K_a:
                    move_left = False
                if event.key == K_RIGHT or event.key == K_d:
                    move_right = False
                if event.key == K_UP or event.key == K_w:
                    move_up = False
                if event.key == K_DOWN or event.key == K_s:
                    move_down = False

            if event.type == MOUSEMOTION:
                # Если мышь движется, переместить игрока к указателю мыши.
                player_rect.centerx = event.pos[0]
                player_rect.centery = event.pos[1]
        # Если необходимо, добавить новых злодеев в верхнюю часть экрана.
        if not reverse_cheat and not slow_cheat:
            baddie_add_counter += 1
        if baddie_add_counter == ADDNEWBADDIERATE:
            baddie_add_counter = 0
            baddie_size = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            new_baddie = {
                'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddie_size), 0 - baddie_size, baddie_size,
                                    baddie_size),
                'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                'surface': pygame.transform.scale(baddie_image, (baddie_size, baddie_size)),
                }

            baddies.append(new_baddie)

        # Перемещение игрока по экрану.
        if move_left and player_rect.left > 0:
            player_rect.move_ip(-1 * PLAYERMOVERATE, 0)
        if move_right and player_rect.right < WINDOWWIDTH:
            player_rect.move_ip(PLAYERMOVERATE, 0)
        if move_up and player_rect.top > 0:
            player_rect.move_ip(0, -1 * PLAYERMOVERATE)
        if move_down and player_rect.bottom < WINDOWHEIGHT:
            player_rect.move_ip(0, PLAYERMOVERATE)

        # Перемещение злодеев вниз.
        for b in baddies:
            if not reverse_cheat and not slow_cheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverse_cheat:
                b['rect'].move_ip(0, -5)
            elif slow_cheat:
                b['rect'].move_ip(0, 1)

        # Удаление злодеев упавших за нижнюю границу экрана.
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)

        window_surface.fill(BACKGROUNDCOLOR)

        draw_text('Счет: %s' % score, font, window_surface, 10, 0)
        draw_text('Рекорд: %s' % top_score, font, window_surface, 10, 40)

        window_surface.blit(player_image, player_rect)

        for b in baddies:
            window_surface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Проверка, попал ли в игрока какой-либо из злодеев.
        if player_has_hit_baddie(player_rect, baddies):
            if score > top_score:
                top_score = score  # set new top score
            break

        main_clock.tick(FPS)

    # Остановка игры и вывод надписи "Игра окончена".
    pygame.mixer.music.stop()
    game_over_sound.play()

    draw_text('ИГРА ОКОНЧЕНА!', font, window_surface, (WINDOWWIDTH // 3), (WINDOWHEIGHT // 3))
    draw_text('Нажмите клавишу для начала новой игры.', font, window_surface, (WINDOWWIDTH // 3) - 150,
              (WINDOWHEIGHT // 3) + 50)
    pygame.display.update()
    wait_for_player_to_press_key()

    game_over_sound.stop()
