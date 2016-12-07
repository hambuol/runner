import pygame


class Backround(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("back.jpg")
        self.rect = self.image.get_rect()
        self.screen = screen
