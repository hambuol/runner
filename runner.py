import pygame,sys
import man
import ground
import enemy
import bottom
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
    myman.rect.topleft = (50, -1000)
    myman.add(manGroup)
    mainsurface.blit(myman.image, myman.rect)


    bottomGroup = pygame.sprite.Group()
    thebottom = bottom.Bottom(mainsurface)
    thebottom.rect.topleft = (0,490)
    thebottom.add(bottomGroup)
    mainsurface.blit(thebottom.image, thebottom.rect)

    groundGroup = pygame.sprite.Group()


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        for x in range(1):
            ypos = random.randint(0,5000)
            xpos = random.randint(600, 2000)
            myground = ground.Ground(mainsurface)
            myground.rect.topleft = (xpos, ypos)
            myground.rect.bottomleft = (xpos, ypos)
            myground.add(groundGroup)
            mainsurface.blit(myground.image, myground.rect)

        pressed = pygame.key.get_pressed()
        # moves mouth if key is pressed
        if pressed[pygame.K_LEFT]:
            myman.left()

        if pressed[pygame.K_RIGHT]:
            myman.right()

        if pressed[pygame.K_SPACE]:
            myman.jump()

        myman.gravity()
        myman.collide_botoom(bottomGroup)
        myman.collide_ground(groundGroup)

        clock = pygame.time.Clock()
        clock.tick(30)
        mainsurface.fill(WHITE)

        for myground in groundGroup:
            mainsurface.blit(myground.image, myground.rect)
            myground.update()
        mainsurface.blit(myman.image, myman.rect)
        for thebottom in bottomGroup:
            mainsurface.blit(thebottom.image, thebottom.rect)

        pygame.display.update()

main()