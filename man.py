import pygame


class Man(pygame.sprite.Sprite):
    """class sets what is needed for spaceship/man """

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 14
        self.speedy = 10
        self.lives = 100
        self.power_up = pygame.mixer.Sound("Power-Up-KP-1879176533.wav")



    def left(self):
        """
        moves spaceship/man left
        :param: none
        :return: none
        """
        if self.rect.left > 0:
            self.rect.left -= self.speedx

    def right(self):
        """
        moves spaceship/man right
        :param: none
        :return: none
        """
        if self.rect.right < self.screen.get_width():
            self.rect.left += self.speedx

    def up(self):
        """
        moves spaceship/man up
        :param: none
        :return:none
        """
        if self.rect.top > 0:
            self.rect.top -= self.speedy

    def down(self):
        """
        moves spaceship/man down
        :param: none
        :return: none
        """
        if self.rect.bottom < self.screen.get_height():
            self.rect.bottom += self.speedy


    def collide(self, spriteGroup):
        """
        collide function takes away 5 from lives
        :param spriteGroup:
        :return: none
        """
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.lives -= 5

    def collide_final(self, spriteGroup):
        """
        collide function takes away 10 from lives
        :param spriteGroup:
        :return: none
        """
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.lives -= 10

    def colide_2(self, spriteGroupa, spriteGroupb):
        """
        collide function adds 50 to lives
        :param spriteGroupa:
        :param spriteGroupb:
        :return: none
        """
        if pygame.sprite.groupcollide(spriteGroupa, spriteGroupb, False, False):
            self.lives += 50
            self.power_up.play()


            








