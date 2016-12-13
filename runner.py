import pygame,sys
import man
import ground
import enemy
import fire
import backround
import score
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
    myend.rect.topleft = (0,-4000)
    myend.add(endGroup)
    mainsurface.blit(myend.image, myend.rect)

    fireGroup = pygame.sprite.Group()
    thefire = fire.Fire(mainsurface, RED)



    ememyGroup = pygame.sprite.Group()
    groundGroup = pygame.sprite.Group()
    clock = pygame.time.Clock()
    end_it = False
    while (end_it == False):
        mainsurface.fill(BLACK)
        myfont = pygame.font.SysFont("Britannic Bold", 40)
        nlabel = myfont.render("Click to start", 1, (255, 0, 0))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                end_it = True
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        mainsurface.blit(nlabel, (300, 200))
        pygame.display.flip()
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


        ypose = random.randint(0,5000)
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





        myman.collide(groundGroup)
        myman.collide(ememyGroup)

        myend.collide(ememyGroup)
        myend.collide(groundGroup)




        mainsurface.fill(WHITE)

        mainsurface.blit(mybackround.image, mybackround.rect)
        for myend in endGroup:
            mainsurface.blit(myend.image, myend.rect)
        for myenemy in ememyGroup:
            mainsurface.blit(myenemy.image, myenemy.rect)
            myenemy.update(groundGroup)
            myenemy.update(fireGroup)


        for myground in groundGroup:
            mainsurface.blit(myground.image, myground.rect)
            myground.update()


        mainsurface.blit(myman.image, myman.rect)
        for thefire in fireGroup:
            mainsurface.blit(thefire.image, thefire.rect)
            thefire.fire()
            if thefire.collide_ground(groundGroup):
                thefire.remove(fireGroup)



        scorefont = pygame.font.SysFont("Britannic Bold", 40)
        scorelable = scorefont.render("Score: {0}".format(thefire.the_score), 1, RED)
        mainsurface.blit(scorelable, (10, 10))






        pygame.display.update()

main()