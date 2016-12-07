import pygame


class Ground(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen):
        super().__init__()
        self.width = 80
        self.height = 10
        self.image = pygame.image.load("asteroid.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 7
        self.speedy = 3


    def update(self):
        self.rect.left -= self.speedx



