import pygame


class Enemy(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen):
        super().__init__()
        self.width = 45
        self.height = 10
        self.image = pygame.image.load("therocket.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 15
        self.speedy = 10


    def update(self, spriteGroup):
        self.rect.left -= self.speedx
        pygame.sprite.spritecollide(self, spriteGroup, True)
