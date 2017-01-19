# written by oliver hamburger
# program is an original game called "star runner"
# last modified 1/19/17

import pygame


class Fire(pygame.sprite.Sprite):
    """class sets what is needed for projectile/fire
    sounds from https://www.freesound.org"""

    def __init__(self, screen, color):
        super().__init__()
        self.image = pygame.image.load("projectile.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 40
        self.speedy = -20
        self.the_score = 0
        self.hit = pygame.mixer.Sound("explosion.wav")
        self.hit_final = pygame.mixer.Sound("Scary_Scream-SoundBible.wav")


    def fire(self):
        """
        adds movement to fire sprite
        :return: none
        """
        self.rect.left += self.speedx

    def collide_ground(self, spriteGroup):
        """
        deletes sprite that it collides with, adds to points and moves the fire sprite off the screen
        :param spriteGroup:
        :return: none
        """
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.rect.top = 4000
            self.the_score += 1
            self.hit.play()

    def collide_final(self, spriteGroup):
        """
        deletes sprite that it collides with, adds to points and moves the fire sprite off the screen
        :param spriteGroup:
        :return: none
        """
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.rect.top = 4000
            self.the_score += 1
            self.hit_final.play()





