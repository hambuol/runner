import pygame
import score


class Fire(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen, color):
        super().__init__()
        #self.width = 20
        #self.height = 10
        self.image = pygame.image.load("projectile.png")
        #self.image.fill(color)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 40
        self.speedy = 0
        self.the_score = score.Score()


    def fire(self):
        self.rect.left += self.speedx

    def collide_ground(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.rect.top = 4000
            self.the_score.increase()

    def collide_enemy(self, spriteGroup):
        pygame.sprite.spritecollide(self, spriteGroup, True)
