import pygame

theClock = pygame.time.Clock()

background = pygame.image.load('поле.jpg')

background_size = background.get_size()
background_rect = background.get_rect()
screen = pygame.display.set_mode(background_size)
width, height = background_size
x = 0
y = 0

x1 = 0
y1 = -height

running = True

while running:
    screen.blit(background, background_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (x, y))
    screen.blit(background, (x1, y1))
    pygame.display.flip()
    pygame.display.update()
    theClock.tick(10)
