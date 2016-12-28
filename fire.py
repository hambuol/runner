import pygame



class Fire(pygame.sprite.Sprite):

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
        self.rect.left += self.speedx

    def collide_ground(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.rect.top = 4000
            self.the_score += 15
            self.hit.play()

    def collide_final(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.rect.top = 4000
            self.the_score += 1
            self.hit_final.play()


    def collide_enemy(self, spriteGroup):
        pygame.sprite.spritecollide(self, spriteGroup, False)



