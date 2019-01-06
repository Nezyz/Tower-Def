import pygame
import sys

pygame.init()
size = width, height = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tower def")
screen.fill(pygame.Color(92, 0, 6))
# Тут скорее всего цикл for для уменьшиния и упрощения кода
circle_width = 0
circle_radius = 0
circle_exists = False
circle_color = (0, 0, 255)
clock = pygame.time.Clock()
circle_pos = (100, 300)
circle_radius = 15
circle_width = 0
pygame.draw.circle(screen, circle_color, circle_pos, circle_radius, circle_width)
pygame.font.init()
fontObj = pygame.font.SysFont('arial', 15)
textSurfaceObj = fontObj.render('1', True, (255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (100, 300)
screen.blit(textSurfaceObj, textRectObj)
circle_width = 0
circle_radius = 0
circle_exists = False
circle_color = (0, 0, 255)
clock = pygame.time.Clock()
circle_pos = (150, 300)
circle_radius = 15
circle_width = 0
pygame.draw.circle(screen, circle_color, circle_pos, circle_radius, circle_width)
pygame.font.init()
fontObj = pygame.font.SysFont('arial', 15)
textSurfaceObj = fontObj.render('2', True, (255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (150, 300)
screen.blit(textSurfaceObj, textRectObj)
circle_width = 0
circle_radius = 0
circle_exists = False
circle_color = (0, 0, 255)
clock = pygame.time.Clock()
circle_pos = (200, 300)
circle_radius = 15
circle_width = 0
pygame.draw.circle(screen, circle_color, circle_pos, circle_radius, circle_width)
pygame.font.init()
fontObj = pygame.font.SysFont('arial', 15)
textSurfaceObj = fontObj.render('3', True, (255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 300)
screen.blit(textSurfaceObj, textRectObj)
circle_width = 0
circle_radius = 0
circle_exists = False
circle_color = (0, 0, 255)
clock = pygame.time.Clock()
circle_pos = (250, 300)
circle_radius = 15
circle_width = 0
pygame.draw.circle(screen, circle_color, circle_pos, circle_radius, circle_width)
pygame.font.init()
fontObj = pygame.font.SysFont('arial', 15)
textSurfaceObj = fontObj.render('4', True, (255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (250, 300)
screen.blit(textSurfaceObj, textRectObj)
circle_width = 0
circle_radius = 0
circle_exists = False
circle_color = (0, 0, 255)
clock = pygame.time.Clock()
circle_pos = (150 * 2, 300)
circle_radius = 15
circle_width = 0
pygame.draw.circle(screen, circle_color, circle_pos, circle_radius, circle_width)
pygame.font.init()
fontObj = pygame.font.SysFont('arial', 15)
textSurfaceObj = fontObj.render('5', True, (255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (150 * 2, 300)
screen.blit(textSurfaceObj, textRectObj)
pygame.display.flip()
clock.tick(30)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
