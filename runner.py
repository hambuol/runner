import pygame,sys
import man
import ground
import enemy
import fire
import backround
import start_screen
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
    pygame.display.set_caption("Star Runner")

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
    thefire = fire.Fire(mainsurface, RED)
    clock = pygame.time.Clock()
    end_it = False
    while (end_it == False):
        clock.tick(30)
        print(clock.get_fps())
        mainsurface.fill(BLACK)
        myfont = pygame.font.SysFont("Britannic Bold", 100)
        slabel1 = myfont.render("Star Runner", 1, (255, 0, 0))
        slabel2 = myfont.render("Click to Play", 1, (0, 0,255))

        ypos = random.randint(0, 1200)
        xpos = (820)
        myground = ground.Ground(mainsurface)
        myground.rect.topleft = (xpos, ypos)
        myground.add(groundGroup)


        ypose = random.randint(0, 5000)
        xpose = (820)
        myenemy = enemy.Enemy(mainsurface)
        myenemy.rect.topleft = (xpose, ypose)
        myenemy.add(ememyGroup)
        mainsurface.blit(mybackround.image, mybackround.rect)
        mainsurface.blit(slabel1, (200, 100))
        mainsurface.blit(slabel2, (200, 200))


        for myend in endGroup:
            mainsurface.blit(myend.image, myend.rect)

        for myenemy in ememyGroup:
            mainsurface.blit(myenemy.image, myenemy.rect)
            myenemy.update(groundGroup)
            myenemy.update(fireGroup)

        for myground in groundGroup:
            mainsurface.blit(myground.image, myground.rect)
            myground.update()
        myend.collide(ememyGroup)
        myend.collide(groundGroup)


        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                for myenemy in ememyGroup:
                    myenemy.remove(ememyGroup)
                for myground in groundGroup:
                    myground.remove(groundGroup)
                end_it = True
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN):

                if (event.key == pygame.K_SPACE):
                        thefire.add(fireGroup)
                        thefire.rect.topleft = (myman.rect.left + 5, myman.rect.top + 10)


        clock.tick(30)
        print(clock.get_fps())

        ypos = random.randint(0, 2400)
        xpos = (920)
        myground = ground.Ground(mainsurface)
        myground.rect.topleft = (xpos, ypos)
        myground.add(groundGroup)
        mainsurface.blit(myground.image, myground.rect)


        ypose = random.randint(0, 10000)
        xpose = (920)
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


        points = thefire.the_score
        mainsurface.fill(WHITE)
        scorefont = pygame.font.SysFont("Britannic Bold", 40)
        scorelable = scorefont.render("Score: {0}".format(points), 1, RED)
        levellable = scorefont.render("Level up!".format(points), 1, RED)

        lives = myman.lives
        liveslable = scorefont.render("Health:".format(lives), 1, RED)
        if lives == 0:
            pygame.quit()
            sys.exit()

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

        for thefire in fireGroup:
            mainsurface.blit(thefire.image, thefire.rect)
            thefire.fire()
            if thefire.collide_ground(groundGroup):
                thefire.remove(fireGroup)
        mainsurface.blit(myman.image, myman.rect)
        mainsurface.blit(scorelable, (10, 10))
        mainsurface.blit(liveslable, (560, 10))
        if points == 20:
            mainsurface.blit(levellable, (100, 100))
            # make harder

        pygame.draw.rect(mainsurface, (RED), (670, 18, lives, 15), 0)









        pygame.display.update()

main()