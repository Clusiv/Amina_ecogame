from game_models import Bin, Trash
import pygame
import time

from os import path, stat
def game_history(screen):
    img_dir = path.join(path.dirname(__file__), 'img')

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    dialogcoord = (1050, 380)

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

    binglass_sprite = pygame.image.load('img/glass.png')
    binmetal_sprite = pygame.image.load('img/metal.png')
    binpaper_sprite = pygame.image.load('img/paper1.png')
    binplastic_sprite = pygame.image.load('img/plastic1.png')

    bin = Bin(290,560, binglass_sprite, 'glass')
    bin2 = Bin(200,560, binmetal_sprite, 'metal')
    bin3 = Bin(110,560, binplastic_sprite, 'plastic')
    bin4 = Bin(20,560, binpaper_sprite, 'paper')

    history = []
    history.append(['привет'])
    history.append(['добро пожаловать в savesummer'])
    history.append(['для начала хочу рассказать', 
            'о экологической проблеме в мире'])
    history.append([
        'экологическая проблема возникла',    
        'в результате взаимодействия', 
        'общества и природы, которое', 
        'приводит к глобальной', 
        'экологической катастрофе',
        ])
    history.append(['люди мусорят, рубят леса,', 'загрязняют воду и воздух'])
    history.append(['это приводит к ужасным ', 'последствиям'])
    history.append(['суть этой игры - научить', 'людей обращаться с мусором'])
    history.append(['смотри как тут грязно...'])
    history.append(['видишь баки?'])
    history.append(['синий - для бумаги '])
    history.append(['желтый - для пластика'])
    history.append(['красный - для металла'])
    history.append(['а зеленый - для стекла'])
    history.append([
        'знаешь, ты бы очень помог',
        'если бы собрал этот мусор', 
        'и рассортировал его по своим местам'])
    history.append([
        'таким образом, мы сможем', 
        'его переработать и создать', 
        'что-нибудь новое и полезное '])
    history.append(['Можешь приступать, а я проверю'])

    state = 0

    def text_blit(state):
        for i, text in enumerate(history[state]):
            screen.blit(text_format(text, font, 16, BLACK), (dialogcoord[0]+ 30 , dialogcoord[1] + 16 + 26 * i))

    def text_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
        return newText

    font = "19363.ttf"
    # font = pygame.font.match_font('Ubuntu Bold')
    font_name = pygame.font.match_font('Ubunti Regular')
    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)



    dialog_sprite = pygame.transform.smoothscale(pygame.image.load('img/dialog.png'), (400, 200))
    mentor_sprite = pygame.image.load('img/mentor1.png')

    def blit_all():
        screen.blit(background, background_rect) 
        screen.blit(dialog_sprite, dialogcoord)
        screen.blit(mentor_sprite, (1418, 572))
        text_blit(state)
        # draw_text(screen, str(score), 20, 20, 10)

    def blit_trash():
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
    
    def blit_bin():
        screen.blit(bin.image,(bin.rect.x, bin.rect.y)) 
        screen.blit(bin2.image,(bin2.rect.x, bin2.rect.y))
        screen.blit(bin3.image,(bin3.rect.x, bin3.rect.y))
        screen.blit(bin4.image,(bin4.rect.x, bin4.rect.y))

    background = pygame.image.load(path.join(img_dir, "fon.png")).convert()
    background_rect = background.get_rect()
    # Load a pictures
    # is_move = False
    # count = 0
    # score = 0
    
    blit_all()
    pygame.display.flip()
    clock = pygame.time.Clock()
    FPS=60
    running = True
    while running:
        

        if state < 7:
            blit_all()
        elif state == 7:
            blit_all()
            blit_trash()
        elif state >= 8:
            blit_all()
            blit_trash()
            blit_bin()
        # screen.blit(background, background_rect) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # pygame.quit()

            # Press the mouse to make the state become movable
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            
            if event.type == pygame.MOUSEBUTTONUP:
                if state + 1 == len(history):
                    running = False
                state += 1

            if event.type == pygame.MOUSEMOTION:
                pass
                
        clock.tick(FPS)
        # all_sprites.draw(screen)

        pygame.display.update()