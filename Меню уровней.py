import pygame
import sys

pygame.init()
x, y = pygame.mouse.get_pos()
print(x, y)
size = width, height = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tower def")
screen.fill(pygame.Color(92, 0, 6))
# Тут скорее всего цикл for для уменьшиния и упрощения кода
circle_width1 = 0
circle_radius1 = 0
circle_exists1 = False
circle_color1 = (0, 0, 255)
clock = pygame.time.Clock()
circle_pos1 = (100, 300)
circle_radius1 = 15
circle_width1 = 0
pygame.draw.circle(screen, circle_color1, circle_pos1, circle_radius1, circle_width1)
pygame.font.init()
fontObj = pygame.font.SysFont('arial', 15)
textSurfaceObj = fontObj.render('1', True, (255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (100, 300)
screen.blit(textSurfaceObj, textRectObj)
circle_width2 = 0
circle_radius2 = 0
circle_exists2 = False
circle_color2 = (0, 0, 255)
clock = pygame.time.Clock()
circle_pos2 = (150, 300)
circle_radius2 = 15
circle_width2 = 0
pygame.draw.circle(screen, circle_color2, circle_pos2, circle_radius2, circle_width2)
pygame.font.init()
fontObj = pygame.font.SysFont('arial', 15)
textSurfaceObj = fontObj.render('2', True, (255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (150, 300)
screen.blit(textSurfaceObj, textRectObj)
circle_width3 = 0
circle_radius3 = 0
circle_exists3 = False
circle_color3 = (0, 0, 255)
clock = pygame.time.Clock()
circle_pos3 = (200, 300)
circle_radius3 = 15
circle_width3 = 0
pygame.draw.circle(screen, circle_color3, circle_pos3, circle_radius3, circle_width3)
pygame.font.init()
fontObj = pygame.font.SysFont('arial', 15)
textSurfaceObj = fontObj.render('3', True, (255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 300)
screen.blit(textSurfaceObj, textRectObj)
circle_width4 = 0
circle_radius4 = 0
circle_exists4 = False
circle_color4 = (0, 0, 255)
clock = pygame.time.Clock()
circle_pos4 = (250, 300)
circle_radius4 = 15
circle_width4 = 0
pygame.draw.circle(screen, circle_color4, circle_pos4, circle_radius4, circle_width4)
pygame.font.init()
fontObj = pygame.font.SysFont('arial', 15)
textSurfaceObj = fontObj.render('4', True, (255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (250, 300)
screen.blit(textSurfaceObj, textRectObj)
circle_width5 = 0
circle_radius5 = 0
circle_exists5 = False
circle_color5 = (0, 0, 255)
clock = pygame.time.Clock()
circle_pos5 = (150 * 2, 300)
circle_radius5 = 15
circle_width5 = 0
pygame.draw.circle(screen, circle_color5, circle_pos5, circle_radius5, circle_width5)
pygame.font.init()
fontObj = pygame.font.SysFont('arial', 15)
textSurfaceObj = fontObj.render('5', True, (255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (150 * 2, 300)
screen.blit(textSurfaceObj, textRectObj)
pygame.display.flip()
clock.tick(30)


def get_click(self, mouse_position):
    x, y = mouse_position
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()
        print(x, y)


while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
