import pygame


class Ground(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen):
        super().__init__()
        self.width = 100
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 5
        self.speedy = 5
        #self.jump = pygame.mixer.Sound("")

    def update(self):
        self.rect.left -= self.speedx



