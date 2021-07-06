from game_history import game_history
from game_option import game
from game_end import game_end
import pygame
from pygame.locals import *
import os
from os import path, putenv
from game_option import game

coord1 = 453, 641
coord2 = 1185, 564
coord3 = 702, 638
coord4 = 333, 214
coord5 = 922, 469
coord6 = 1449, 624
coord7 = 969, 649
coord8 = 325, 751
coord9 = 591, 159

img_dir = path.join(path.dirname(__file__), 'img')
# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=1500
screen_height=800
screen=pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load(path.join(img_dir, "fon.png")).convert()
background_rect = background.get_rect()

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText

def is_in_rect(pos, rect):
    x, y = pos
    rx, ry, rw, rh = rect
    if (rx <= x <= rx+rw) and (ry <= y <= ry+rh):
        return True
    return False

 
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
 
# Game Fonts
font = "19151.ttf"


clock = pygame.time.Clock()
FPS=60
# Main Menu
def main_menu():
 
    menu=True
    selected="start"
    text_start=text_format("START", font, 75, black)
    text_quit=text_format("QUIT", font, 75, black)
    title=text_format("  SAVE SUMMER", font, 90, gray)


    title_rect=title.get_rect()
    start_rect=text_start.get_rect()
    quit_rect=text_quit.get_rect()

    start_w, start_h = text_start.get_size()
    quit_w, quit_h = text_quit.get_size()

    while menu:



        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            # if event.type==pygame.KEYDOWN:
            #     if event.key==pygame.K_UP:
            #         selected="start"
            #     elif event.key==pygame.K_DOWN:
            #         selected="quit"
            #     if event.key==pygame.K_RETURN:
            #         if selected=="start":
            #             game_history(screen)
            #             game(screen)
            #         if selected=="quit":
            #             pygame.quit()
            #             quit()

            if event.type == pygame.MOUSEBUTTONUP:
                if is_in_rect(event.pos, (screen_width/2 - (start_rect[2]/2), 300 , start_w, start_h)):
                    game_history(screen)
                    game(screen)
                    game_end(screen)
                elif is_in_rect(event.pos, (screen_width/2 - (quit_rect[2]/2), 400 , quit_w, quit_h)):
                    pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                
                if is_in_rect(event.pos, (screen_width/2 - (start_rect[2]/2), 300 , start_w, start_h)):
                    text_start=text_format("START", font, 75, white)
                elif is_in_rect(event.pos, (screen_width/2 - (quit_rect[2]/2), 400 , quit_w, quit_h)):
                    text_quit=text_format("QUIT", font, 75, white)
                else:
                    text_start=text_format("START", font, 75, black)
                    text_quit=text_format("QUIT", font, 75, black)

        # Main Menu UI
        screen.blit(background, background_rect) 

        # if selected=="start":
        #     text_start=text_format("START", font, 75, white)
        # else:
        #     text_start = text_format("START", font, 75, black)
        # if selected=="quit":
        #     text_quit=text_format("QUIT", font, 75, white)
        # else:
        #     text_quit = text_format("QUIT", font, 75, black)
 

 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 400))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")
    

main_menu()
pygame.quit()
quit()