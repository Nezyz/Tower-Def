import pygame

pygame.init()

white = (255, 255, 255)
active_color = pygame.Color('dodgerblue1')
inactive_color = pygame.Color('dodgerblue4')
font = pygame.font.SysFont('arial', 50)


def draw_button(button, screen):
    pygame.draw.rect(screen, button['color'], button['rect'])
    screen.blit(button['text'], button['text rect'])


def create_button(x, y, w, h, text, callback):
    text_surf = font.render(text, True, white)
    button_rect = pygame.Rect(x, y, w, h)
    text_rect = text_surf.get_rect(center=button_rect.center)
    button = {
        'rect': button_rect,
        'text': text_surf,
        'text rect': text_rect,
        'color': inactive_color,
        'callback': callback,
    }
    return button


def main():
    screen = pygame.display.set_mode((450, 550))
    clock = pygame.time.Clock()
    done = False

    def start():
        pass

    def exitt():
        nonlocal done
        done = True

    def settings():
        pass

    def info():
        pass

    # Кнопки, размер и расположение, название, функции, которые срабатывают по нажатию
    button1 = create_button(100, 100, 250, 80, 'Start', start)
    button2 = create_button(100, 200, 250, 80, 'Settings', settings)
    button3 = create_button(100, 300, 250, 80, 'Info', info)
    button4 = create_button(100, 400, 250, 80, 'Exit', exitt)
    # Список с кнопками
    button_list = [button1, button2, button3, button4]

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
                        button['color'] = active_color
                    else:
                        button['color'] = inactive_color

        screen.fill(white)
        for button in button_list:
            draw_button(button, screen)
        pygame.display.update()
        clock.tick(30)


main()
pygame.quit()
