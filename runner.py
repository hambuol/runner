import pygame,sys
import man
import ground
import enemy
import fire
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

    endGroup = pygame.sprite.Group()
    myend = ground.End(mainsurface, RED)
    myend.rect.topleft = (20,-4000)
    myend.add(endGroup)
    mainsurface.blit(myend.image, myend.rect)

    fireGroup = pygame.sprite.Group()
    #thefire = fire.Fire(mainsurface, RED)


    ememyGroup = pygame.sprite.Group()



    groundGroup = pygame.sprite.Group()

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN):

                if (event.key == pygame.K_SPACE):
                    thefire = fire.Fire(mainsurface, RED)
                    thefire.add(fireGroup)
                    thefire.rect.topleft = (myman.rect.left + 5, myman.rect.top + 20)




        clock.tick(30)
        print(clock.get_fps())



        ypos = random.randint(0, 1200)
        xpos = (900)
        myground = ground.Ground(mainsurface)
        myground.rect.topleft = (xpos, ypos)
        myground.add(groundGroup)
        mainsurface.blit(myground.image, myground.rect)


        ypose = random.randint(0,4000)
        xpose = (900)
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

        if len(fireGroup) == 1:
            thefire.fire()



        #myman.collide(groundGroup)
        #myman.collide(ememyGroup)

        myend.collide(ememyGroup)
        myend.collide(groundGroup)



        mainsurface.fill(WHITE)

        mainsurface.blit(mybackround.image, mybackround.rect)
        for myend in endGroup:
            mainsurface.blit(myend.image, myend.rect)
        for myenemy in ememyGroup:
            mainsurface.blit(myenemy.image, myenemy.rect)
            myenemy.update(groundGroup)


        for myground in groundGroup:
            mainsurface.blit(myground.image, myground.rect)
            myground.update()


        mainsurface.blit(myman.image, myman.rect)
        for thefire in fireGroup:
            mainsurface.blit(thefire.image, thefire.rect)
        if len(fireGroup) == 1:
            thefire.collide_ground(groundGroup)
            thefire.remove(fireGroup)

        pygame.display.update()

main()