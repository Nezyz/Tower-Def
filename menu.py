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


def create_battleground():
    global width, height
    background = pygame.image.load('field_battle.jpg')

    background_size = background.get_size()
    width, height = background.get_size()
    background_rect = background.get_rect()
    screen = pygame.display.set_mode(background_size)
    width, height = background_size
    screen.blit(background, (0, 0))


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


def play_game():
    import play


def start():
    return True


def exit():
    pygame.quit()
    sys.exit()


def info():
    import info_about_game


button_start = create_button(100, 30, 250, 120, 'Играть', play_game)
button_about_play = create_button(100, 210, 250, 120, 'Об игре', info)
button_exit = create_button(100, 390, 250, 120, 'Выход', exit)
button_list = [button_start, button_about_play, button_exit]

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
