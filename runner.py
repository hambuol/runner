import pygame,sys
import man
import ground
import enemy
import fire
import backround
import special
import random
import final
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
    myman.rect.topleft = (50, 250)
    myman.add(manGroup)
    mainsurface.blit(myman.image, myman.rect)

    endGroup = pygame.sprite.Group()
    myend = ground.End(mainsurface, RED)
    myend.rect.topleft = (0, -4000)
    myend.add(endGroup)
    mainsurface.blit(myend.image, myend.rect)

    starGroup = pygame.sprite.Group()
    mystar = special.Special(mainsurface)

    fireGroup = pygame.sprite.Group()
    thefire = fire.Fire(mainsurface, RED)

    finalGroup = pygame.sprite.Group()
    ememyGroup = pygame.sprite.Group()
    groundGroup = pygame.sprite.Group()
    thefire = fire.Fire(mainsurface, RED)
    clock = pygame.time.Clock()
    pygame.mixer.music.load("imperial_march.wav")
    pygame.mixer.music.play(-1)
    end_it = False
    while (end_it == False):
        clock.tick(30)
        print(clock.get_fps())
        mainsurface.fill(BLACK)
        myfont = pygame.font.SysFont("Britannic Bold", 100)
        myfont1 = pygame.font.SysFont("Britannic Bold", 50)
        slabel1 = myfont.render("Star Runner", 1, (255, 0, 0))
        slabel2 = myfont1.render("Click or press space to Play", 1, (0, 0,255))

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
        mainsurface.blit(slabel2, (150, 200))



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
            if event.type == MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_SPACE]:
                for myenemy in ememyGroup:
                    myenemy.remove(ememyGroup)
                for myground in groundGroup:
                    myground.remove(groundGroup)
                end_it = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN): 
                if (event.key == pygame.K_p):
                    pygame.mixer.music.pause()
                if (event.key == pygame.K_u):
                    pygame.mixer.music.unpause()
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
                if (event.key == pygame.K_p):
                    pygame.mixer.music.pause()
                if (event.key == pygame.K_u):
                    pygame.mixer.music.unpause()





        clock.tick(30)
        #print(clock.get_fps())

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
        myman.collide_final(finalGroup)


        myend.collide(ememyGroup)
        myend.collide(groundGroup)

        level = 1
        points = thefire.the_score
        if points >= 15:
            level += 1
        if points >= 30:
            level += 1
        if points >= 45:
            level += 1
        if points >= 60:
            level += 1
        if points >= 75:
            level += 1
        if points >= 90:
            level += 1
        if points >= 105:
            level += 1
        if points >= 120:
            level += 1
        if points >= 135:
            level += 1
        if points >= 150:
            level = "Final"

        mainsurface.fill(WHITE)
        scorefont = pygame.font.SysFont("Britannic Bold", 40)
        scorelable = scorefont.render("Score: {0}".format(points), 1, RED)
        levellable = scorefont.render("Level: {}".format(level), 1, RED)
        overlable = myfont.render("Game Over", 1, (255, 0, 0))
        winlable = myfont.render("You Won!", 1, (255, 0, 0))
        mainscreenlable = scorefont.render("Press Space to return to home screen", 1, (0, 0, 255))
        lives = myman.lives
        liveslable = scorefont.render("Health:".format(lives), 1, RED)

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
            thefire.collide_ground(groundGroup)


        win = pygame.mixer.Sound("Ta_Da-SoundBible.wav")
        if points >= 200:
            myman.rect.top = 4000
            myman.rect.left = 4000
            mainsurface.blit(winlable, (200, 200))
            mainsurface.blit(mainscreenlable, (120, 275))
            pygame.mixer.music.stop()
            win.play()
            for myfinal in finalGroup:
                myfinal.remove(finalGroup)
            if pressed[pygame.K_SPACE]:
                main()

        mainsurface.blit(myman.image, myman.rect)
        mainsurface.blit(scorelable, (10, 10))
        mainsurface.blit(liveslable, (10, 473))
        mainsurface.blit(levellable, (630, 10))

        if points >= 15:
            for myground in groundGroup:
                myground.level_up()
        if points >= 30:
            for myenemy in ememyGroup:
                myenemy.level_up()
        if points >= 45:
            for myground in groundGroup:
                myground.level_up()
        if points >= 60:
            for myenemy in ememyGroup:
                myenemy.level_up()
        if points >= 75:
            for myground in groundGroup:
                myground.level_up()
        if points >= 90:
            for myenemy in ememyGroup:
                myenemy.level_up()
        if points >= 105:
            for myground in groundGroup:
                myground.level_up()
        if points >= 120:
            for myenemy in ememyGroup:
                myenemy.level_up()
        if points >= 135:
            for myground in groundGroup:
                myground.level_up()
        if points >= 150:
            for myenemy in ememyGroup:
                myenemy.remove(ememyGroup)
            for myground in groundGroup:
                myground.remove(groundGroup)
            y = random.randint(0, 2500)
            x = 920
            myfinal = final.Final(mainsurface)
            myfinal.rect.topleft = (x, y)
            myfinal.add(finalGroup)
            mainsurface.blit(myfinal.image, myfinal.rect)
            for myfinal in finalGroup:
                mainsurface.blit(myfinal.image, myfinal.rect)
                myfinal.update(manGroup)
            if thefire.collide_final(finalGroup):
                thefire.remove(fireGroup)

        if points == 15:
            mystar.rect.topleft = (920, random.randint(5, 495))
            mystar.add(starGroup)

        if points == 45:
            mystar.rect.topleft = (920, random.randint(5, 495))
            mystar.add(starGroup)

        if points == 75:
            mystar.rect.topleft = (920, random.randint(5, 495))
            mystar.add(starGroup)

        if points == 105:
            mystar.rect.topleft = (920, random.randint(5, 495))
            mystar.add(starGroup)

        if points == 135:
            mystar.rect.topleft = (920, random.randint(5, 495))
            mystar.add(starGroup)

        for mystar in starGroup:
            mainsurface.blit(mystar.image, mystar.rect)
            mystar.update()
        myman.colide_2(starGroup, manGroup)
        pygame.draw.rect(mainsurface, (RED), (115, 480, lives, 15), 0)
        print(lives)

        if lives == 0 or lives < 0:
            myman.rect.top = 4000
            myman.rect.left = 4000
            mainsurface.blit(overlable, (200, 200))
            mainsurface.blit(mainscreenlable, (120, 275))
            pygame.mixer.music.stop()
            if pressed[pygame.K_SPACE]:
                main()

        pygame.display.update()
main()
