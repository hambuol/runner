import pygame
import fire


class Special(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen):
        super().__init__()
        self.width = 20
        self.height = 20
        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 25
        self.speedy = 0


    def update(self):
        self.rect.left -= self.speedx



