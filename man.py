import pygame


class Man(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("apple.jpg")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 10
        self.speedy = 10
        #self.jump = pygame.mixer.Sound("")


    def jump(self):
        pass

    def double_jump(self):
        pass