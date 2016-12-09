import pygame



class Ground(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

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
        self.rect.left -= self.speedx


    def collide(self, spriteGroup):
        pygame.sprite.spritecollide(self, spriteGroup, True)

class End(pygame.sprite.Sprite):
        """class sets what is needed for mouth"""

        def __init__(self, screen, color):
            super().__init__()
            self.width = 1
            self.height = 8000
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.screen = screen

        def collide(self, spriteGroup):
            pygame.sprite.spritecollide(self, spriteGroup, True)






