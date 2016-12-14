import pygame


class Enemy(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen):
        super().__init__()
        self.width = 45
        self.height = 10
        self.image = pygame.image.load("rocket.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 7
        self.speedy = 0


    def update(self, spriteGroup):
        self.rect.left -= self.speedx
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.rect.left += 7

