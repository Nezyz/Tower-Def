import pygame
import os
import sys

pygame.init()
size = width, height = (500, 500)
screen = pygame.display.set_mode(size)
image = pygame.Surface([100, 100])
image.fill(pygame.Color("red"))
punkts = [(120, 140, 'Play', (250, 250, 30), (250, 30, 250), 0),
          (130, 210, 'Quit', (250, 250, 30), (250, 30, 250), 1)]
class Menu():
    def __init__(self, punkts=[120, 140, 'punkt', (250, 250, 30), (250, 30, 250), 0]):
        self.punkts = punkts

    def menu(self):
        done = True
        punkt = 0
        while done:
            screen.fill((0, 100, 200))
            for j in pygame.event.get():
                if j.type == pygame.QUIT:
                    sys.exit()
                if j.type == pygame.KEYDOWN:
                    if j.key == pygame.K_ESCAPE:
                        sys.exit()
                    if j.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                        if j.key == pygame.K_DOWN:
                            if punkt < len(self.punkts) - 1:
                                punkt += 1
                if j.type == pygame.MOUSEBUTTONDOWN and j.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


image = load_image("страшила.png")
image1 = pygame.transform.scale(image, (200, 100))
image2 = pygame.transform.scale(image, (100, 200))
screen.blit(image, (10, 10))
game = Menu(punkts)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
    game.menu()
pygame.quit()
