import pygame,sys
import man
import ground
import enemy
import bottom
import backround
import random
import time
from pygame.locals import *
def main():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 500
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    pygame.init()
    mainsurface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption("Runner")

    backroundGroup = pygame.sprite.Group()
    mybackround = backround.Backround(mainsurface)
    mybackround.rect.topleft = (0, 0)
    mybackround.add(backroundGroup)
    mainsurface.blit(mybackround.image, mybackround.rect)

    manGroup = pygame.sprite.Group()
    myman = man.Man(mainsurface)
    myman.rect.topleft = (50,250)
    myman.add(manGroup)
    mainsurface.blit(myman.image, myman.rect)


    bottomGroup = pygame.sprite.Group()
    thebottom = bottom.Bottom(mainsurface)
    thebottom.rect.topleft = (0,490)
    thebottom.add(bottomGroup)
    mainsurface.blit(thebottom.image, thebottom.rect)

    ememyGroup = pygame.sprite.Group()



    groundGroup = pygame.sprite.Group()


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN):

                if (event.key == pygame.K_SPACE):
                    myman.jump()
        for x in range(1):
            ypos = random.randint(0, 5000)
            xpos = random.randint(700, 3000)
            myground = ground.Ground(mainsurface)
            myground.rect.topleft = (xpos, ypos)
            myground.add(groundGroup)
            mainsurface.blit(myground.image, myground.rect)

        for x in range(1):
            ypose = random.randint(0,5000)
            xpose = random.randint(850,9000)
            myenemy = enemy.Enemy(mainsurface)
            myenemy.rect.topleft = (xpose, ypose)
            myenemy.add(ememyGroup)
            mainsurface.blit(myenemy.image, myenemy.rect)

        pressed = pygame.key.get_pressed()
        # moves mouth if key is pressed
        if pressed[pygame.K_LEFT]:
            myman.left()

        if pressed[pygame.K_RIGHT]:
            myman.right()

        if pressed[pygame.K_UP]:
            myman.up()

        if pressed[pygame.K_DOWN]:
            myman.down()


        #myman.gravity()
        myman.collide_botoom(bottomGroup)
        myman.collide_ground(groundGroup)
        myman.collide_enemy(ememyGroup)

        clock = pygame.time.Clock()
        clock.tick(30)
        mainsurface.fill(WHITE)
        mainsurface.blit(mybackround.image, mybackround.rect)
        for myenemy in ememyGroup:
            mainsurface.blit(myenemy.image, myenemy.rect)
            myenemy.update()

        for myground in groundGroup:
            mainsurface.blit(myground.image, myground.rect)
            myground.update()
        mainsurface.blit(myman.image, myman.rect)
        for thebottom in bottomGroup:
            mainsurface.blit(thebottom.image, thebottom.rect)

        pygame.display.update()

main()