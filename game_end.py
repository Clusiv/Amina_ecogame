from game_models import Bin, Trash
import pygame
import time

from os import path, stat
def game_end(screen):
    img_dir = path.join(path.dirname(__file__), 'img')

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    dialogcoord = (350, 380)

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

    def blit_bin():
        screen.blit(bin.image,(bin.rect.x, bin.rect.y)) 
        screen.blit(bin2.image,(bin2.rect.x, bin2.rect.y))
        screen.blit(bin3.image,(bin3.rect.x, bin3.rect.y))
        screen.blit(bin4.image,(bin4.rect.x, bin4.rect.y))

    bin = Bin(290,560, binglass_sprite, 'glass')
    bin2 = Bin(200,560, binmetal_sprite, 'metal')
    bin3 = Bin(110,560, binplastic_sprite, 'plastic')
    bin4 = Bin(20,560, binpaper_sprite, 'paper')

    end = []
    end.append(['воу'])
    end.append(['не плохо'])
    end.append(['отличная работа'])
    end.append(['должен сказать что я не ожидал '])
    end.append(['что ты заметишь вазу у окна'])
    end.append(['но ты справился, молодец'])
    end.append(['НО'])
    end.append(['увы, это ещё не всё'])
    end.append(['теперь ты должен запомнить '])
    end.append(['чтобы сохронить такой вид везде'])
    end.append(['НИ В КОЕМ СЛУЧАЕ не мусори '])
    end.append([
        'рядом обязательно найдётся',
        'мусорная корзина'
        ])
    end.append(['в общем..'])
    end.append(['спасибо что прибрал здесь всё'])
    end.append(['и спасибо за игру'])
    end.append(['надеюсь ещё увидемся'])
    end.append(['пока'])

    state = 0

    def text_blit(state):
        for i, text in enumerate(end[state]):
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
    mentor_sprite =  pygame.transform.smoothscale(pygame.image.load('img/mentor1.png'), (97, 200))

    def blit_all():
        screen.blit(background, background_rect) 
        screen.blit(dialog_sprite, dialogcoord)
        screen.blit(mentor_sprite, (700, 552))
        blit_bin()
        text_blit(state)

    background = pygame.image.load(path.join(img_dir, "fon2.png")).convert()
    background_rect = background.get_rect()
    blit_all()
    pygame.display.flip()
    clock = pygame.time.Clock()
    FPS=60
    running = True
    while running:
        

        # if state < 7:
        #     blit_all()
        # elif state == 7:
        #     blit_all()
        #     blit_trash()
        # elif state >= 8:
        #     blit_all()
        #     blit_trash()
        #     blit_bin()
        # screen.blit(background, background_rect) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # pygame.quit()

            # Press the mouse to make the state become movable
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            
            if event.type == pygame.MOUSEBUTTONUP:
                if state + 1 == len(end):
                    running = False
                else: 
                    state += 1

            if event.type == pygame.MOUSEMOTION:
                pass
                
        clock.tick(FPS)
        # all_sprites.draw(screen)
        blit_all()
        pygame.display.update()
    