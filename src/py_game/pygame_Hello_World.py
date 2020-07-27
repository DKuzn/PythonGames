import pygame
import sys
from pygame.locals import *

pygame.init()

window_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Привет, мир!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

basic_font = pygame.font.SysFont(None, 48)

text = basic_font.render('Привет, мир!', True, WHITE, BLUE)
text_rect = text.get_rect()
text_rect.centerx = window_surface.get_rect().centerx
text_rect.centery = window_surface.get_rect().centery

window_surface.fill(WHITE)

pygame.draw.polygon(window_surface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

pygame.draw.line(window_surface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(window_surface, BLUE, (120, 60), (60, 120))
pygame.draw.line(window_surface, BLUE, (60, 120), (120, 120), 4)

pygame.draw.circle(window_surface, BLUE, (300, 50), 20, 0)

pygame.draw.ellipse(window_surface, RED, (300, 250, 40, 80), 1)

pygame.draw.rect(window_surface, RED, (text_rect.left - 20, text_rect.top - 20,
                                       text_rect.width + 40, text_rect.height + 40))

pix_array = pygame.PixelArray(window_surface)
pix_array[480][380] = BLACK
del pix_array

window_surface.blit(text, text_rect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
