import pygame, sys


class Man(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("fighter.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 14
        self.speedy = 10


    def jump(self):
        if self.rect.top < self.screen.get_height():
            self.rect.bottom -= self.speedy + 100


    def left(self):
        """
        moves mouth left
        :param: none
        :return: none
        """
        if self.rect.left > 0:
            self.rect.left -= self.speedx

    def right(self):
        """
        moves mouth right
        :param: none
        :return: none
        """
        if self.rect.right < self.screen.get_width():
            self.rect.left += self.speedx

    def up(self):
        """
        moves mouth up
        :param: none
        :return:none
        """
        if self.rect.top > 0:
            self.rect.top -= self.speedy

    def down(self):
        """
        moves mouth down
        :param: none
        :return: none
        """
        if self.rect.bottom < self.screen.get_height():
            self.rect.bottom += self.speedy

    def gravity(self):
        if self.rect.bottom < 495:
            self.rect.bottom += self.speedy





    def collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            pygame.quit()
            sys.exit()

            








