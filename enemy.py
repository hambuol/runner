# written by oliver hamburger
# program is an original game called "star runner"
# last modified 1/19/17

import pygame


class Enemy(pygame.sprite.Sprite):
    """class sets what is needed for rockets/enemy"""

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
        """
        updates enemy sprite and slows down speed if it hit anything
        :param spriteGroup:
        :return: none
        """
        self.rect.left -= self.speedx
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.rect.left += 7

    def level_up(self):
        """
        speeds up enemy sprite for the next level
        :return: none
        """
        self.rect.left -= 5