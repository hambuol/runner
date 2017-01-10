import pygame


class Ground(pygame.sprite.Sprite):
    """class sets what is needed for ground/asteroids"""

    def __init__(self, screen):
        super().__init__()
        self.width = 80
        self.height = 10
        self.image = pygame.image.load("asteroid.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 5
        self.speedy = 3

    def update(self):
        """
        updates the movement of the ateroids
        :return: none
        """
        self.rect.left -= self.speedx

    def level_up(self):
        """
        makes speed of asteroids faster for next level
        :return: none
        """
        self.rect.left -= 2

class End(pygame.sprite.Sprite):
        """class sets what is needed for mouth"""

        def __init__(self, screen, color):
            super().__init__()
            self.width = 1
            self.height = 10000
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.screen = screen
            self.hit = pygame.mixer.Sound("explosion.wav")

        def collide(self, spriteGroup):
            """
            collide function deletes sprites if it collides with end sprite
            :param spriteGroup:
            :return:
            """
            pygame.sprite.spritecollide(self, spriteGroup, True)







