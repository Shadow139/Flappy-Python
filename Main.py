__author__ = 'Wiktor'

from random import randint
from GameSettings import *
from Color import *

import pygame
import time
import Bird
import Block
import Background
import Animation
import ParallaxScrolling
import sys
import Spike


### Definitions

pygame.font.init()
text_small = pygame.font.Font('freesansbold.ttf',20)
text_large = pygame.font.Font('freesansbold.ttf',150)

pygame.init()
surface = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Awaaaysomeee Game!")

clock = pygame.time.Clock()


def gameLoop():
    game_over = False

    background1 = Background.Background('Assets/background.png',0,0)
    background2 = Background.Background('Assets/background.png',screen_width,0)

    background_scroller1 = ParallaxScrolling.ParallaxScrolling(background1,background2,-4)

    background3 = Background.Background('Assets/groundSnow.png',0,410)
    background4 = Background.Background('Assets/groundSnow.png',screen_width,410)

    background_scroller2 = ParallaxScrolling.ParallaxScrolling(background3,background4,-6)

    anim = Animation.Animation("Assets/grumpy/", 0.1, 0.125)

    player = Bird.Bird(150, 200, 0, 6, anim)

    block = Block.Block(screen_width,0,75,randint(0,(screen_height/2)),180,3,0,clr_white)
    #spike = Spike.Spike(screen_width,0,75,randint(0,(screen_height/2)) ,180,3,0,'Assets/spikeLong.png','Assets/spikeLongFlip.png')

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(1)

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    player.y_velocity = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.y_velocity = 5

        player.update()

        surface.fill(clr_black)
        background_scroller1.render(surface,screen_width)
        background_scroller2.render(surface,screen_width)

        player.render(surface)

        block.update()
        block.renderBlocks(surface)


        #spike.update()
        #spike.render(surface)


        if player.y > screen_height - player.height or player.y < 0 :
            gameOver()

        #if player.rect.colliderect(spike.rect1):
        #    print('collision with 1')

        #if player.rect.colliderect(spike.rect2):
        #    print('collision with 2')

        if player.x + player.width > block.x:
            if player.x < block.x + block.width:
                if player.y < block.height:
                    if(player.x - player.width < block.x + block.width):
                        gameOver()

        if player.x + player.width > block.x:
            if player.y + player.height > block.height + block.gap:
                if player.x < block.x + block.width:
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

gameLoop()

pygame.quit()
quit()