import pygame,sys
import man
import ground
import enemy
import random
import time
from pygame.locals import *
def main():
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    WHITE = (255, 255, 255)
    pygame.init()
    mainsurface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption("Runner")

    manGroup = pygame.sprite.Group()
    myman = man.Man(mainsurface)
    myman.rect.topleft = (50, 400)
    myman.add(manGroup)
    mainsurface.blit(myman.image, myman.rect)

    groundGroup = pygame.sprite.Group()












    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        for x in range(1):
            ypos = random.randint(0,500)
            xpos = random.randint(600, 1000)
            myground = ground.Ground(mainsurface)
            myground.rect.topleft = (xpos, ypos)
            myground.add(groundGroup)
            mainsurface.blit(myground.image, myground.rect)


        clock = pygame.time.Clock()
        clock.tick(50)
        mainsurface.fill(WHITE)

        for myground in groundGroup:
            mainsurface.blit(myground.image, myground.rect)
            myground.update()
        mainsurface.blit(myman.image, myman.rect)

        pygame.display.update()

main()