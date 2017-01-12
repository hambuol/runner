import pygame


class Final(pygame.sprite.Sprite):
    """class sets what is needed for final
    image from https://commons.wikimedia.org/wiki/File:Aliensmiley.svg"""

    def __init__(self, screen):
        super().__init__()
        self.width = 45
        self.height = 40
        self.image = pygame.image.load("alien1.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 20
        self.speedy = 0


    def update(self, spriteGroup):
        """
        updates movement of final sprite
        :param spriteGroup:
        :return: none
        """
        self.rect.left -= self.speedx






