import pygame

pygame.init()
WHITE = (255, 255, 255)
ACTIVE_COLOR = pygame.Color('dodgerblue1')
INACTIVE_COLOR = pygame.Color('dodgerblue4')
FONT = pygame.font.SysFont('arial', 50)

black = [2, 2, 2]
white = [255, 255, 255]
red = [92, 0, 6]
green = [0, 255, 0]
blue = [0, 0, 255]


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


size = [400, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("About")

done = False
clock = pygame.time.Clock()

while done == False:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(red)
    font = pygame.font.Font(None, 25)
    font1 = pygame.font.Font(None, 35)
    text = font.render("v.1.0", True, black)
    text_2 = font.render("Tower-Def", True, black)
    text_3 = font1.render("Авотры игры: Старков Андрей,", True, black)
    text_4 = font1.render("Забавников Даниил", True, black)
    screen.blit(text, [175, 480])
    screen.blit(text_2, [150, 10])
    screen.blit(text_3, [10, 250])
    screen.blit(text_4, [60, 285])
    pygame.display.flip()

pygame.quit()
