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

class Text():
    def __init__(self, text, font, surface_menu, x, y):
        self.name = text
        self.text_obj = font.render(text, 1, font_color)
        self.text_rect = self.text_obj.get_rect()
        self.text_rect.topleft = (x, y)
        surface_menu.blit(self.text_obj, self.text_rect)

    def get_click(self, mouse_position):
        x,y = mouse_position
        if self.text_rect.topleft[0]  < x <= self.text_rect.topleft [0]+ self.text_rect.w and self.text_rect.topleft[1]  < y <= self.text_rect.topleft [1]+ self.text_rect.h:
            print("Click in", self.name )

position_text = [((surface_width / 2) - 65, (surface_height / 2) - 90),
                 ((surface_width / 2) - 50, (surface_height / 2) + 10)]
start = Text('Start', font, surface_menu, *position_text[0])
exit = Text('Exit', font, surface_menu, *position_text[1])

pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if pygame.event.wait().type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            start.get_click(event.pos)
            exit.get_click(event.pos)
    pygame.display.flip()
pygame.quit()