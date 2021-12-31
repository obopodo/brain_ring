import pygame
import sys
import numpy as np

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLUE = (0,0,255)
BLUISH = (75,75,255)
YELLOW =(255,255,0)
BLACK = (0, 0, 0)
GREEN = (np.array((70, 115, 70)) * 1.5).astype(int)

# SCREEN
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
dispay_info = pygame.display.Info()
WIDTH, HEIGHT = dispay_info.current_w, dispay_info.current_h

# BG
path_to_bg = "imgs\\NYslide1.jpg"
bg = pygame.image.load(path_to_bg)
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
screen.blit(bg, (0, 0))
pygame.display.update()

# FONT
pygame.font.init()
font_size = 500
myfont = pygame.font.SysFont('Segoe UI', font_size, italic=True)
myfont2 = pygame.font.SysFont('Segoe UI', font_size, italic=True)
font_color = WHITE

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
events = []
teams = ['Дед', 'Мороз'] # TODO read from text file
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif  event.type == pygame.JOYBUTTONDOWN:
            if  event.button == 0: # press A button to display team name
                events.append(event.instance_id)
                textsurface = myfont.render(teams[events[0]], False, font_color)
                # textsurface = bg = pygame.transform.scale(textsurface, (WIDTH // 3, HEIGHT // 3))
                text_w = textsurface.get_width()
                text_h = textsurface.get_height()
                screen.blit(textsurface, ((WIDTH - text_w) // 2, (HEIGHT -  1.1 * text_h) // 2))

                pygame.display.update()
                # clock.tick(10)

            elif  event.button == 7 and len(events): # press start to reset
                if event.instance_id == events[0]:
                    events = []
                    # screen.fill(BLACK)
                    screen.blit(bg, (0, 0))
                    pygame.display.update()

        elif  event.type == pygame.JOYBUTTONUP:
            if  event.button == 0:
                pass
