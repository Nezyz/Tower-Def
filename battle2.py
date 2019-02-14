import pygame
import os
import random
size = width, height = 600, 300
pygame.font.init()
screen = pygame.display.set_mode(size)
#FONT = pygame.font.SysFont('arial', 50)
black = [2, 2, 2]
ai_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
ai_sprites = pygame.sprite.Group()
fire_sprite = pygame.sprite.Group()
fire = None
experience = 0
hp_p = 1000
ai = []


def load_images(path, colorkey=None):
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name).convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
            image = image.convert_alpha()
        images.append(image)
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
    tower_def = load_images('tower_def', -1)

    def __init__(self, x, y, number):
        super().__init__(all_sprites)
        self.image = Tower.tower_def[1]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.index = 0

    def get_xy(self):
        return self.rect.topleft


class Fire(pygame.sprite.Sprite):
    arrow = load_images('tower_def', -1)

    def __init__(self, x, y, target):
        super().__init__(all_sprites)
        self.add(fire_sprite)
        self.image = Fire.arrow[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.index = 0
        self.current_tower = 0
        self.damage = 25
        self.vx = int(target[0] / 10)
        self.vy = int(target[1] / 10)

    def update(self):
        self.rect.left += self.vx
        self.rect.top += self.vy
        for ai in ai_sprites:
            if pygame.sprite.collide_rect(self, ai):
                ai.damage(self.damage)

                self.kill()


class Bashnya(pygame.sprite.Sprite):
    town = load_images('tower_def', -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Bashnya.town[2]
        self.rect = self.image.get_rect()
        self.rect.topleft = (300, 171)
        self.index = 0
        self.hp = 1000
        self.mana = 100
        self.score = 0

    def damage(self, damage):
        self.hp -= damage

    def update(self):
        print(self.hp)
        hp_p = self.hp
        for ai in ai_sprites:
            if pygame.sprite.collide_rect(self, ai):
                self.damage(ai.my_damage)
        if self.hp <= 0:

            print("game over")


class AI(pygame.sprite.Sprite):
    fire = None

    def __init__(self, images):
        super().__init__(all_sprites)
        self.add(ai_sprites)
        size = (32, 32)

        self.health = 100
        self.my_damage = 10
        self.experience = 0

        self.rect = pygame.Rect((width - 50, random.randint(0, height - 32)), size)
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

        self.hp_monster = 100

    def damage(self, damage):
        self.hp_monster -= damage
        print(self.hp_monster)

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
        self.vx = -5
        if self.rect.left < 405:
            self.vx = 0
        self.rect.left = self.rect.left + self.vx

        self.rect.top = self.rect.top + int((town.rect.top - self.rect.top) / 30)

    def update(self):
        self.update_time_dependent(clock.tick(50) / 1100)
        self.run_ai()
        if self.hp_monster <= 0:
            town.score += 1
            all_sprites.remove(self)
            self.kill()


create_battleground()
running = True
count_ai = 3
dt = clock.tick(50) /100000000
images_ai = load_images('images1', -1)
for i in range(count_ai):
    a_current = AI(images=images_ai)
    print(a_current)
    ai.append(a_current)
tower = Tower(75, 0, 0)
tower2 = Tower(75, 265, 1)
tower3 = Tower(145, 135, 0)
town = Bashnya()
fire = []
time = 0
while running:
    time += 5
    print(time)
    #FONT = pygame.font.SysFont('arial', 50)
    #text = FONT.render(town.score, True, black)
    #screen.blit(text, [175, 480])
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x_new, y_new = event.pos
                if y_new >= 0 and y_new < 135 and x_new > 250:
                    x, y = tower.get_xy()
                    fire.append(Fire(*tower.get_xy(), [x_new - x, y_new - y]))
                elif y_new >= 135 and y_new < 265 and x_new > 250:
                    x, y = tower3.get_xy()
                    fire.append(Fire(*tower3.get_xy(), [x_new - x, y_new - y]))
                elif y_new >= 265 and x_new > 250:
                    x, y = tower2.get_xy()
                    fire.append(Fire(*tower2.get_xy(), [x_new - x, y_new - y]))

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    if len(ai_sprites) < 3 and time > 100:
        time = 0
        experience += 100
        new_ai = random.randint(2, 6)
        for j in range(new_ai):
            ai.append(AI(images=images_ai))
    create_battleground()
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(60)
    if town.hp <= 0:
        fon_img = load_images('gameover', -1)
        fon = pygame.transform.scale(fon_img[0], (width, height))
        screen.fill(pygame.Color(0, 0, 0))
        screen.blit(fon, (0, 0))
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("EXPERIENCE:", 1, (255, 255, 0))
        screen.blit(label, (20, 20))
        label_2 = myfont.render(str(experience), 1, (255, 255, 0))
        screen.blit(label_2, (20, 40))
        running = False
print(count_ai)

running2 = True
while running2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running2 = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            running2 = False
            pygame.quit()
    pygame.display.flip()
pygame.quit()
