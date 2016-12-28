import pygame


class Final(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.width = 45
        self.height = 40
        self.image = pygame.image.load("alien.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 20
        self.speedy = 0


    def update(self, spriteGroup):
        self.rect.left -= self.speedx
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.rect.left += 7



