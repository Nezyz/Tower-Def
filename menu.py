import pygame
pygame.init()

WHITE = (255, 255, 255)
ACTIVE_COLOR = pygame.Color('dodgerblue1')
INACTIVE_COLOR = pygame.Color('dodgerblue4')
FONT = pygame.font.SysFont('arial', 50)


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


def main():
    screen = pygame.display.set_mode((450, 550))
    clock = pygame.time.Clock()
    done = False

    def start():
        import menu_lvl

    def exit():
        nonlocal done
        done = True


    def info():
        pass
    button1 = create_button(100, 100, 250, 80, 'Start', start)
    button3 = create_button(100, 250, 250, 80, 'Info', info)
    button4 = create_button(100, 400, 250, 80, 'Exit', exit)
    button_list = [button1, button3, button4]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in button_list:
                        if button['rect'].collidepoint(event.pos):
                            button['callback']()
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


main()
pygame.quit()
