# written by oliver hamburger
# program is an original game called "star runner"
# last modified 1/19/17

import pygame


class Special(pygame.sprite.Sprite):
    """class sets what is needed for power-up star/special"""

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 25
        self.speedy = 0


    def update(self):
        """
        updates special sprite for movement
        :return: none
        """
        self.rect.left -= self.speedx



