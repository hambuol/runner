import pygame


class Bottom(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen, color):
        super().__init__()
        self.width = 20
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 40
        self.speedy = 0


    def fire(self):
            self.rect.left += self.speedx

    def collide_ground(self, spriteGroup):
        pygame.sprite.spritecollide(self, spriteGroup, True)
