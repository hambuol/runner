import pygame


class Bottom(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen):
        super().__init__()
        self.width = 500
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 3
        self.speedy = 3