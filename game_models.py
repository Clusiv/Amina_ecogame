import pygame

BLACK=(0, 0, 0)

class Trash(pygame.sprite.Sprite):
        def __init__(self, x,y, image, sort):
            pygame.sprite.Sprite.__init__(self)
            self.image = image
            self.image.set_colorkey(BLACK)
            self.rect  = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.sort = sort
            self.is_move = False
        # def update(self):
        #     self.kill()
        
class Bin(pygame.sprite.Sprite):
    def __init__(self, x, y, image, sort):
        pygame.sprite.Sprite.__init__(self)
        # self.image = meteor_img
        # Выбираем изображение метеора случайным образом
        self.image_orig = image
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect  = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sort = sort