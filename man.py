import pygame


class Man(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("apple.jpg")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 10
        self.speedy = 5


    def up(self):
        if self.rect.top < self.screen.get_height():
            self.rect.bottom -= self.speedy



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


    def collide_botoom(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.rect.bottom -= self.speedy


