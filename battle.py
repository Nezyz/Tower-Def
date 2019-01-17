import pygame
import os
import random

size = width, height = 300,300

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()




def load_images(path, colorkey=None):
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name).convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        images.append(image)
        image = image.convert_alpha()
    return images
def create_battleground():
    global width, height
    background = pygame.image.load('field_battle.jpg')

    background_size = background.get_size()
    width, height = background.get_size()
    background_rect = background.get_rect()
    screen = pygame.display.set_mode(background_size)
    width, height = background_size
    screen.blit(background, (0, 0))

class Tower(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        pass
    def draw(self):
        pass

class AI(pygame.sprite.Sprite):
    def __init__(self, images):
        super(AI, self).__init__()

        size = (32, 32)

        self.health = 100
        self.damage = 10



        self.rect = pygame.Rect((width-50, random.randint(0,height - 32)), size)
        self.images = images
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]
        self.index = 0
        self.image = images[self.index]

        self.velocity = pygame.math.Vector2(0, 0)

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

    def get_pos(self):
        return self.rect.top, self.rect.left

    def update_time_dependent(self, dt):
        if self.velocity.x > 0:
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update_frame_dependent(self):
        if self.velocity.x > 0:
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)
    def run_ai(self):
        self.vx = -3
        if  self.rect.left < 125:
            self.vx = 0
        self.rect.left = self.rect.left + self.vx

    def update(self, dt):
        self.update_time_dependent(dt)
        self.run_ai()


create_battleground()
tower = Tower()
running = True
count_ai = 3
dt = clock.tick(50) / 1100
ai=[]
images_ai = load_images('images1', -1)
for i in range(count_ai):
    ai.append(AI(images=images_ai))
all_sprites = pygame.sprite.Group(ai)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    create_battleground()
    all_sprites.draw(screen)
    all_sprites.update(dt)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(25)
print(ai)
for player in ai:
    print(player.get_pos())