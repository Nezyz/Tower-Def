'''import pygame
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

pygame.quit()'''



import pygame
pygame.init()

RED = (255, 0, 0)
ACTIVE_COLOR = pygame.Color('dodgerblue1')
INACTIVE_COLOR = pygame.Color('dodgerblue4')
FONT = pygame.font.SysFont('arial', 50)


def draw_button(button, screen):
    pygame.draw.rect(screen, button['color'], button['rect'])
    screen.blit(button['text'], button['text rect'])


def create_button(x, y, w, h, text, callback):
    text_surf = FONT.render(text, True, RED)
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

        screen.fill(RED)
        for button in button_list:
            draw_button(button, screen)
        pygame.display.update()
        clock.tick(30)


main()
pygame.quit()
