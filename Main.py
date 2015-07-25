import ParallaxScrolling

__author__ = 'Wiktor'

from random import randint
from Color import *

import pygame
import time
import Bird
import Block
import Background

### Definitions

screen_width = 800
screen_height = 480

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

    background_scroller = ParallaxScrolling.ParallaxScrolling(background1,background2,-4)

    player = Bird.Bird(150,200, 0, 5,'Assets/bird.png')

    block = Block.Block(screen_width,0,75,randint(0,(screen_height/2)),180,3,0,clr_white)


    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    player.y_velocity = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.y_velocity = 5

        player.y += player.y_velocity

        surface.fill(clr_black)
        background_scroller.render(surface,screen_width)
        player.render(surface,player.x,player.y,player.asset)

        makeBlocks(block.x,block.y,block.width,block.height,block.gap)
        block.x -= block.x_velocity

        if player.y > screen_height - player.height or player.y < 0 :
            gameOver()

        if block.x < (-1 * block.width):
            block.x = screen_width
            block.height = randint(0,(screen_height/2))

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

gameLoop()

pygame.quit()
quit()