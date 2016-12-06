import pygame


class Ground(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen):
        super().__init__()
        self.width = 70
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 3
        self.speedy = 3


    def update(self):
        self.rect.left -= self.speedx



