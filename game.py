import pygame
import os
import random
import sys

pygame.init()

WHITE = (255, 255, 255)
ACTIVE_COLOR = pygame.Color(215, 215, 215, 0)
INACTIVE_COLOR = pygame.Color(27, 31, 28, 0)
FONT = pygame.font.SysFont('arial', 50)
pygame.display.set_caption("Tower def")

done = False

running = True
screen = pygame.display.set_mode((450, 550))
clock = pygame.time.Clock()
done = False
ai_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
ai_sprites = pygame.sprite.Group()
fire_sprite = pygame.sprite.Group()


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


class Particle(pygame.sprite.Sprite):
    fire = load_images("blood", -1)
    for scale in (3, 5, 10):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.time_life = 5
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos

    def draw(self):
        if self.time_life > 0:
            r = screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.time_life -= 1

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.time_life < 0:
            self.kill()


def create_particles(position):
    particle_count = 10
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


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

        self.hp = 1000
        self.image = Tower.tower_def[1]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.index = 0

        self.mana = 100

    def get_xy(self):
        return self.rect.topleft

    def update(self):
        self.hp = tower.hp
        if self.hp <= 250:
            self.kill()


class Fire(pygame.sprite.Sprite):
    arrow = load_images('tower_def', -1)
    a = load_images('blood', -1)
    flag_fire = True

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
        self.hp = tower.hp
        if self.hp <= 250:
            self.flag_fire = False
            self.kill()
        self.rect.left += self.vx
        self.rect.top += self.vy
        for ai in ai_sprites:
            if pygame.sprite.collide_rect(self, ai):
                ai.damage(self.damage)
                create_particles((self.rect.left + 90, self.rect.top + 30))
                self.kill()
                self.image = Fire.a[0]
                self.image = pygame.Surface((10, 10))
                self.image.fill(pygame.Color("red"))


class Bashnya(pygame.sprite.Sprite):
    town = load_images('tower_def', -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Bashnya.town[2]
        self.rect = self.image.get_rect()
        self.rect.topleft = (320, 171)
        self.index = 0
        self.flag = True
        self.hp = 1000
        self.score = 0

    def update(self):
        if tower.hp <= 750:
            all_sprites.remove(self)
            self.kill()
            self.flag = False


class HPBar(pygame.sprite.Sprite):
    def __init__(self, t):
        super().__init__(all_sprites)
        self.image = pygame.Surface((819, 10))
        self.image.fill(pygame.Color("red"))
        self.rect = ((0, 0), (819, 10))
        self.tower = t

    def update(self, *args):
        value = int((819) * (self.tower.hp / 1000))
        if value > 0:
            self.image = pygame.Surface((value, 10))
            self.image.fill(pygame.Color("red"))
            self.rect = (0, 0, value, 10)


class ManaBar(pygame.sprite.Sprite):
    def __init__(self, t):
        super().__init__(all_sprites)
        self.image = pygame.Surface((819, 380))
        self.image.fill(pygame.Color("blue"))
        self.rect = ((819, 380), (0, 0))
        self.tower = t

    def update(self, *args):
        value = int((819) * (self.tower.mana / 1000))
        if value > 0:
            self.image = pygame.Surface((value, 10))
            self.image.fill(pygame.Color("blue"))
            self.rect = (0, 423, 0, value)


class Death(pygame.sprite.Sprite):
    fire = None

    def __init__(self, images):
        super().__init__(all_sprites)
        self.add(ai_sprites)
        size = (32, 32)

        self.my_damage = 7
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

        self.animation_frames = 2
        self.current_frame = 0

        self.hp_monster = 200

    def damage(self, damage):
        self.hp_monster -= damage

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
        self.vx = -7
        if self.rect.left < 425 and tower.hp >= 750:
            tower.hp -= self.my_damage
            self.vx = 0
        elif self.rect.left != 425 and tower.hp >= 750:
            self.vx = -7
        elif self.rect.left <= 300 and tower.hp >= 250:
            tower.hp -= self.my_damage
            self.vx = 0
        elif self.rect.left != 300 and tower.hp >= 250:
            self.vx = -7
        elif self.rect.left <= 150:
            tower.hp -= self.my_damage
            self.vx = 0

        self.rect.left = self.rect.left + self.vx

        self.rect.top = self.rect.top + int((town.rect.top - self.rect.top) / 30)

    def update(self):
        self.update_time_dependent(clock.tick(50) / 1100)
        self.run_ai()
        if self.hp_monster <= 0:
            town.score += 2
            all_sprites.remove(self)
            self.kill()


class Shaman(pygame.sprite.Sprite):
    fire = None

    def __init__(self, images):
        super().__init__(all_sprites)
        self.add(ai_sprites)
        size = (32, 32)

        self.my_damage = 6
        self.experience = 0

        self.rect = pygame.Rect((width - 50, random.randint(0, height - 32)), size)
        self.images = images
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]
        self.index = 0
        self.image = images[self.index]

        self.velocity = pygame.math.Vector2(0, 0)

        self.animation_time = 0.07
        self.current_time = 0

        self.animation_frames = 2
        self.current_frame = 0

        self.hp_monster = 150

    def damage(self, damage):
        self.hp_monster -= (damage + 5)

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
        self.vx = -6
        if self.rect.left <= 425 and tower.hp >= 750:
            tower.hp -= self.my_damage
            self.vx = 0
        elif self.rect.left != 425 and tower.hp >= 750:
            self.vx = -6
        elif self.rect.left <= 300 and tower.hp >= 250:
            tower.hp -= self.my_damage
            self.vx = 0
        elif self.rect.left != 300 and tower.hp >= 250:
            self.vx = -6
        elif self.rect.left <= 150:
            tower.hp -= self.my_damage
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


class Drago(pygame.sprite.Sprite):
    fire = None

    def __init__(self, images):
        super().__init__(all_sprites)
        self.add(ai_sprites)
        size = (32, 32)

        self.my_damage = 6
        self.experience = 0

        self.rect = pygame.Rect((width - 50, random.randint(0, height - 32)), size)
        self.images = images
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]
        self.index = 0
        self.image = images[self.index]

        self.velocity = pygame.math.Vector2(0, 0)

        self.animation_time = 0.07
        self.current_time = 0

        self.animation_frames = 3
        self.current_frame = 0

        self.hp_monster = 600

    def damage(self, damage):
        self.hp_monster -= (damage + 9)

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
        if self.rect.left <= 425 and tower.hp >= 750:
            tower.hp -= self.my_damage
            self.vx = 0
        elif self.rect.left != 425 and tower.hp >= 750:
            self.vx = -5
        elif self.rect.left <= 300 and tower.hp >= 250:
            tower.hp -= self.my_damage
            self.vx = 0
        elif self.rect.left != 300 and tower.hp >= 250:
            self.vx = -5
        elif self.rect.left <= 150:
            tower.hp -= self.my_damage
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


def draw_button(button, screen):
    pygame.draw.rect(screen, button['color'], button['rect'])
    screen.blit(button['text'], button['text rect'])


def create_button(x, y, w, h, text, callback):
    text_surf = FONT.render(text, True, WHITE)
    button_rect = pygame.Rect(x, y, w, h)
    text_rect = text_surf.get_rect(center=button_rect.center)
    button = {
        'rect': button_rect,
        'text': text_surf,
        'text rect': text_rect,
        'color': INACTIVE_COLOR,
        'callback': callback,
    }
    return button


def start():
    return True


def exit():
    pygame.quit()
    sys.exit()


def info():
    import info_about_game


button1 = create_button(100, 100, 250, 80, 'Start', start)
button3 = create_button(100, 250, 250, 80, 'Info', info)
button4 = create_button(100, 400, 250, 80, 'Exit', exit)
button_list = [button1, button3, button4]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for button in button_list:
                    if button['rect'].collidepoint(event.pos):
                        done = button['callback']()
        elif event.type == pygame.MOUSEMOTION:
            for button in button_list:
                if button['rect'].collidepoint(event.pos):
                    button['color'] = ACTIVE_COLOR
                else:
                    button['color'] = INACTIVE_COLOR

    screen.fill(WHITE)
    for button in button_list:
        draw_button(button, screen)
    pygame.display.update()
    clock.tick(30)

pygame.quit()

size = width, height = 600, 300
pygame.font.init()
screen = pygame.display.set_mode(size)
black = [2, 2, 2]

pygame.display.set_caption("Tower def")
fire = None
experience = 0
hp_p = 1000
ai = []
ai_death = []
ai_shaman = []
ai_drago = []
regulPlaysound = pygame.mixer.init()
pygame.mixer.music.load("1.wav")
pygame.mixer.Channel(1).play(pygame.mixer.Sound(file="2.wav"))
regulPlaysound = True
volume = 1
create_battleground()
running = True
count_ai = 3
count_ai_death = 2
count_ai_shaman = 2
count_ai_drago = 1
dt = clock.tick(50) / 100000000
images_ai = load_images('images1', -1)
images_ai_death = load_images('death', -1)
images_ai_shaman = load_images('shaman', -1)
images_ai_drago = load_images('drago', -1)

for i in range(count_ai_death):
    death_current = Death(images=images_ai_death)
    ai_death.append(death_current)
for i in range(count_ai_shaman):
    shaman_current = Shaman(images=images_ai_shaman)
    ai_shaman.append(shaman_current)

for i in range(count_ai_drago):
    drago_current = Drago(images=images_ai_drago)
    ai_drago.append(drago_current)

tower = Tower(75, 0, 0)
tower2 = Tower(75, 265, 1)
tower3 = Tower(145, 135, 0)
town = Bashnya()
hpbar = HPBar(tower)
manabar = ManaBar(tower)
fire = []
time = 0
time_2 = 0
while running:
    if tower.mana < 100:
        tower.mana += 0.1
    time += 5
    time_2 += 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and tower.mana >= 75 and tower.hp >= 250:
                tower.mana -= 10
                tower.hp += 100

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x_new, y_new = event.pos
                if y_new >= 0 and y_new < 135 and x_new > 250 and town.hp > 250:
                    x, y = tower.get_xy()
                    fire.append(Fire(*tower.get_xy(), [x_new - x, y_new - y]))
                    regulPlaysound = pygame.mixer.init()
                    pygame.mixer.music.load("vstrl2.mp3")
                    pygame.mixer.music.play()
                    regulPlaysound = True
                    volume = 1
                elif y_new >= 135 and y_new < 265 and x_new > 250 and tower.hp > 250:
                    x, y = tower3.get_xy()
                    fire.append(Fire(*tower3.get_xy(), [x_new - x, y_new - y]))
                    regulPlaysound = pygame.mixer.init()
                    pygame.mixer.music.load("vstrl2.mp3")
                    pygame.mixer.music.play()
                    regulPlaysound = True
                elif y_new >= 265 and x_new > 250 and tower.hp > 250:
                    x, y = tower2.get_xy()
                    fire.append(Fire(*tower2.get_xy(), [x_new - x, y_new - y]))
                    regulPlaysound = pygame.mixer.init()
                    pygame.mixer.music.load("vstrl2.mp3")
                    pygame.mixer.music.play()
                    regulPlaysound = True
    if tower.hp >= 750 and town.flag == False:
        town = Bashnya()

    if len(ai_sprites) < 2 and time > 35 and time_2 > 20:
        time = 0
        time_2 = 0
        experience += 100
        new_shaman = random.randint(1, 3)
        for a in range(new_shaman):
            ai_shaman.append(Shaman(images=images_ai_shaman))
    if len(ai_sprites) < 3 and time > 40 and time_2 > 53:
        time = 0
        time_2 = 0
        experience += 100
        new_drago = random.randint(1, 3)
        for a in range(new_drago):
            ai_drago.append(Drago(images=images_ai_drago))
    if len(ai_sprites) < 4 and time > 55 and time_2 > 70:
        time = 0
        time_2 = 0
        experience += 100
        new_death = random.randint(1, 2)
        for g in range(new_death):
            ai_death.append(Death(images=images_ai_death))
    create_battleground()
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(60)
    if tower.hp <= 0:
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

running2 = True
while running2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            exit()
            running2 = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            exit()
            running2 = False

    pygame.display.flip()

pygame.quit()
