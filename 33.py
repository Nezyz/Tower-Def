import pygame
import sys

pygame.font.init()

color = (51, 51, 51)
font_color = (255, 255, 153)
high_color = (153, 102, 255)
font = pygame.font.SysFont('arial', 72)
surface_width = 800
surface_height = 600

surface_menu = pygame.display.set_mode([surface_width, surface_height])

pygame.display.set_caption("Test")

surface_menu.fill(color)


def DrawText(text, font, surface_menu, x, y):
    text_obj = font.render(text, 1, font_color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface_menu.blit(text_obj, text_rect)


DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 90)
DrawText('Exit', font, surface_menu, (surface_width / 2) - 50, (surface_height / 2) + 10)

pygame.display.update()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
