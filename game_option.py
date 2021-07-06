from game_models import Bin, Trash
import pygame
import time
import os, random
from os import path, urandom

def game(screen):
    img_dir = path.join(path.dirname(__file__), 'img')

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    dialogcoord = (1220, 520)

    WRONG = ['Ты выбрал не тот бак', 'Этот бак не подходит']
    RIGHT = ['Отлично', 'Молодец']
    answer = ''

    def text_blit(text):
        # for i, text in enumerate(text_list):
        screen.blit(text_format(text, font, 16, BLACK), (dialogcoord[0]+ 19 , dialogcoord[1]+14))

    def text_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
        return newText

    font = "18959.ttf"
    font_name = pygame.font.match_font('arial')
    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def blit_all():
        screen.blit(background, background_rect) 
        screen.blit(bin.image,(bin.rect.x, bin.rect.y)) 
        screen.blit(bin2.image,(bin2.rect.x, bin2.rect.y))
        screen.blit(bin3.image,(bin3.rect.x, bin3.rect.y))
        screen.blit(bin4.image,(bin4.rect.x, bin4.rect.y))
        screen.blit(cup.image, (cup.rect.x,cup.rect.y))
        screen.blit(papercup.image, (papercup.rect.x,papercup.rect.y))
        screen.blit(papercup2.image, (papercup2.rect.x,papercup2.rect.y))
        screen.blit(bottle.image, (bottle.rect.x,bottle.rect.y))
        screen.blit(bottle2.image, (bottle2.rect.x,bottle2.rect.y))
        screen.blit(plasticbottle.image, (plasticbottle.rect.x,plasticbottle.rect.y))
        screen.blit(pizza_box.image, (pizza_box.rect.x,pizza_box.rect.y))
        screen.blit(metal_bottle.image, (metal_bottle.rect.x,metal_bottle.rect.y))
        screen.blit(metal_bottle2.image, (metal_bottle2.rect.x,metal_bottle2.rect.y))
        screen.blit(vase.image, (vase.rect.x,vase.rect.y))
        
        screen.blit(dialog_sprite, dialogcoord)
        text_blit(answer)
        screen.blit(mentor_sprite, (1418, 572))
        draw_text(screen, str(score), 20, 20, 10)

    def is_in_rect(pos, rect):
        x, y = pos
        rx, ry, rw, rh = rect
        if (rx <= x <= rx+rw) and (ry <= y <= ry+rh):
            return True
        return False

    

    background = pygame.image.load(path.join(img_dir, "fon.png")).convert()
    background_rect = background.get_rect()

    # Load a pictures
    cup_sprite = pygame.image.load('img/Sprite-0002.png')
    papercup_sprite = pygame.image.load('img/bbbb.png')
    papercup2_sprite = pygame.image.load('img/papercup2.png')
    bottle_sprite = pygame.image.load('img/bottle.png')
    bottle2_sprite = pygame.image.load('img/bottle2.png')
    plasticbottle_sprite = pygame.image.load('img/bbbb2.png')
    pizza_sprite = pygame.image.load('img/pizza_box.png')
    metalbottle_sprite = pygame.image.load('img/metal_bottle.png')
    metalbottle2_sprite = pygame.image.load('img/metal_bottle2.png')
    vase_sprite = pygame.image.load('img/vase.png')

    binglass_sprite = pygame.image.load('img/glass.png')
    binmetal_sprite = pygame.image.load('img/metal.png')
    binpaper_sprite = pygame.image.load('img/paper1.png')
    binplastic_sprite = pygame.image.load('img/plastic1.png')

    mentor_sprite = pygame.image.load('img/mentor1.png')
    dialog_sprite = pygame.transform.smoothscale(pygame.image.load('img/dialog.png'), (240, 60))

    trash = pygame.sprite.Group()
    cup = Trash(453, 641,cup_sprite, 'metal')
    papercup = Trash(1185, 564, papercup_sprite, 'paper')
    papercup2 = Trash(702, 638, papercup2_sprite, 'paper')
    bottle = Trash(333, 214, bottle_sprite,'glass')
    bottle2 = Trash(922, 469, bottle2_sprite, 'plastic')
    plasticbottle = Trash(507, 633, plasticbottle_sprite, 'plastic')
    pizza_box = Trash(969, 649, pizza_sprite, 'paper')
    metal_bottle = Trash(325, 751, metalbottle_sprite, 'metal')
    metal_bottle2 = Trash(591, 159, metalbottle2_sprite, 'metal')
    vase = Trash(171, 458, vase_sprite, 'glass')
    trash.add(cup, papercup, papercup2, bottle, bottle2, plasticbottle, pizza_box, metal_bottle, metal_bottle2, vase)

    bins = pygame.sprite.Group()
    bin = Bin(290,560, binglass_sprite, 'glass')
    bin2 = Bin(200,560, binmetal_sprite, 'metal')
    bin3 = Bin(110,560, binplastic_sprite, 'plastic')
    bin4 = Bin(20,560, binpaper_sprite, 'paper')
    bins.add(bin, bin2, bin3, bin4)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(bins, trash)

    count = 0
    score = 0
    
    blit_all()
    pygame.display.flip()

    clock = pygame.time.Clock()
    FPS=60

    running = True
    while running:

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # Press the mouse to make the state become movable
            if event.type == pygame.MOUSEBUTTONDOWN:
                for t in trash:
                    w,h = t.image.get_size()
                    if is_in_rect(event.pos, (t.rect.x, t.rect.y, w, h)):
                        t.is_move = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                for t in trash:
                    t.is_move = False
                if score == 50:
                    running = False
                hits = pygame.sprite.groupcollide(bins,trash,False, False)
                if hits :
                    print(type(hits))
                    count += 1
                    print("Collided" + str(count))
                    for _bin, _trash in hits.items():

                        print(f'_bin = {_bin.sort}')
                        print(f'_trash = {_trash[0].sort}')
                        if _bin.sort == _trash[0].sort  and not _trash[0].is_move:

                            print('Matching')
                            score += 5
                            _trash[0].rect.x = 1000
                            _trash[0].rect.y = 1000
                            answer = random.choice(RIGHT)
                        else:
                            answer = random.choice(WRONG)
                # print('cup: ', cup.rect.x, cup.rect.y)
                # print('papercup: ', papercup.rect.x, papercup.rect.y)
                # print('papercup2: ', papercup2.rect.x, papercup2.rect.y)
                # print('bottle: ', bottle.rect.x, bottle.rect.y)
                # print('bottle2: ', bottle2.rect.x, bottle2.rect.y)
                # print('plasticbottle: ', plasticbottle.rect.x, plasticbottle.rect.y)
                # print('pizza_pox: ', pizza_box.rect.x, pizza_box.rect.y)
                # print('metal_bottle: ', metal_bottle.rect.x, metal_bottle.rect.y)
                # print('metal_bottle2: ', metal_bottle2.rect.x, metal_bottle2.rect.y)
                # print('vase: ', vase.rect.x, vase.rect.y)

            if event.type == pygame.MOUSEMOTION:
                for t in trash:
                    if t.is_move:
                        x, y = event.pos
                        t_w, t_h = t.image.get_size()
                        # Ensure that the mouse is in the center of the picture
                        t.rect.y = y-t_h/2
                        t.rect.x = x-t_w/2

            
        blit_all()
        clock.tick(FPS)
        all_sprites.draw(screen)
        pygame.display.update()


# pygame.init()

# # Center the Game Application
# os.environ['SDL_VIDEO_CENTERED'] = '1'

# # Game Resolution
# screen_width=1500
# screen_height=800
# screen=pygame.display.set_mode((screen_width, screen_height))

# game(screen)