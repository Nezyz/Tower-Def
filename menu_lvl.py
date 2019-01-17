import pygame
import sys

pygame.init()
x, y = pygame.mouse.get_pos()
print(x, y)
size = width, height = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tower def")
screen.fill(pygame.Color(92, 0, 6))
fontObj = []
textRectObj = []
textSurfaceObj = []
name = []
current = 0
for i in range(4):
    for j in range(5):
        circle_width1 = 0
        circle_radius1 = 0
        circle_exists1 = False
        circle_color1 = (0, 0, 255)
        clock = pygame.time.Clock()
        circle_pos1 = (50 + j * 50, 200 + i * 50)
        circle_radius1 = 15
        circle_width1 = 0
        pygame.draw.circle(screen, circle_color1, circle_pos1, circle_radius1, circle_width1)
        pygame.font.init()
        fontObj.append(pygame.font.SysFont('arial', 15))
        textSurfaceObj.append(fontObj[current].render(str(current + 1), True, (255, 255, 255)))
        textRectObj.append(textSurfaceObj[current].get_rect())
        textRectObj[current].center = (50 + j * 50, 200 + i * 50)
        screen.blit(textSurfaceObj[current], textRectObj[current])
        name.append(str(current + 1))
        current += 1
pygame.display.flip()
clock.tick(30)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(textRectObj)):
                if textRectObj[i].collidepoint(event.pos):
                    print(name[i])

    pygame.display.flip()

pygame.quit()
