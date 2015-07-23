from random import randint

__author__ = 'Wiktor'

import pygame
import time

clr_black = (0,0,0)
clr_white = (255,255,255)

screen_width = 800
screen_height = 600

pygame.font.init()
text_small = pygame.font.Font('freesansbold.ttf',20)
text_large = pygame.font.Font('freesansbold.ttf',150)

pygame.init()

surface = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Awaaaysomeee Game!")

clock = pygame.time.Clock()


def gameLoop():
    game_over = False

    bird_x = 150
    bird_y = 200
    bird_width = 100
    bird_height = 43

    bird_y_move = 5

    blck_x = screen_width
    blck_y = 0
    blck_width = 75
    blck_height = randint(0,(screen_height/2))
    blck_gap = 125
    blck_move = 3

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    bird_y_move = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bird_y_move = 5

        bird_y += bird_y_move

        surface.fill(clr_black)
        bird(bird_x,bird_y,img)

        makeBlocks(blck_x,blck_y,blck_width,blck_height,blck_gap)
        blck_x -= blck_move

        if bird_y > screen_height - bird_height or bird_y < 0 :
            gameOver()

        if blck_x < (-1 * blck_width):
            blck_x = screen_width
            blck_height = randint(0,(screen_height/2))

        if bird_x + bird_width > blck_x:
            if bird_x < blck_x + blck_width:
                print('upper x')
                if bird_y < blck_height:
                    print('y cross upper')
                    if(bird_x - bird_width < blck_x + blck_width):
                        print('game over UPPER')
                        gameOver()

        if bird_x + bird_width > blck_x:
            print('x crossover')
            if bird_y + bird_height > blck_height+blck_gap:
                print('Y crossover lower')
                if bird_x < blck_x + blck_width:
                    print('game over LOWER')
                    gameOver()

        pygame.display.update()
        clock.tick(60)

def gameOver():
    msgOnScreen('Game Over!')

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue

        return event.key

    return None

def makeBlocks(x_block,y_block,block_width,block_height,gap):
    pygame.draw.rect(surface,clr_white,[x_block,y_block,block_width,block_height])
    pygame.draw.rect(surface,clr_white,[x_block,y_block + block_height + gap,block_width,screen_height])

def makeTextObjs(message,font):
    textSurface = font.render(message,True,clr_white)
    return textSurface, textSurface.get_rect()

def msgOnScreen(message):
    titleTextSurf,titleTextRect = makeTextObjs(message,text_large)
    titleTextRect.center = screen_width/2, screen_height/2
    surface.blit(titleTextSurf,titleTextRect)

    subTitleTextSurf,subTitleTextRect = makeTextObjs('Press any key to continue!',text_small)
    subTitleTextRect.center = screen_width/2, (screen_height/2 + 100)
    surface.blit(subTitleTextSurf,subTitleTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    gameLoop()

def bird(x,y,image):
    surface.blit(image,(x,y))

img = pygame.image.load('Assets/bird.png')

gameLoop()


pygame.quit()
quit()