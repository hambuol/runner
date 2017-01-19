# written by oliver hamburger
# program is an original game called "star runner"
# last modified 1/19/17

import pygame


class Backround(pygame.sprite.Sprite):
    """class sets what is needed for backround"""

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("backround.jpg")
        self.rect = self.image.get_rect()
        self.screen = screen
