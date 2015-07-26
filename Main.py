import MessageOnScreen

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


pygame.init()
surface = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Awaaaysomeee Game!")

clock = pygame.time.Clock()


def gameLoop():
    game_over = False
    paused = False

    space_pressed = True

    pause_bckgrnd = pygame.Surface((screen_width,screen_height), pygame.SRCALPHA, 32)
    pause_bckgrnd.fill((0, 0, 0, 150))

    sound = pygame.mixer.Sound('Assets/Audio/TheLoomingBattle_0.OGG')
    sound.play()

    pause_message = MessageOnScreen.MessageOnScreen('Paused',screen_width/2, screen_height/2,text_large,clr_white)
    gameOver_message = MessageOnScreen.MessageOnScreen('Game Over!',screen_width/2, screen_height/2,text_medium,clr_darkgrey)
    pressAny_message = MessageOnScreen.MessageOnScreen('Press any key to continue!',screen_width/2, (screen_height/2 + 100) ,text_small,clr_darkgrey)


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

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    paused = not(paused)
                if event.key == pygame.K_SPACE:
                    space_pressed = True

        if not paused:
            space = pygame.key.get_pressed()[pygame.K_SPACE]

            if space and space_pressed:
                player.y_velocity = -45
                space_pressed = False
            else:
                player.y_velocity = 5

            background_scroller1.render(surface,screen_width)
            background_scroller2.render(surface,screen_width)

            player.update()
            player.render(surface)

            block.update()
            block.renderBlocks(surface)

            #spike.update()
            #spike.render(surface)

            if player.y > screen_height - player.height + 20 or player.y < 0 :
                gameOver(gameOver_message,pressAny_message)

            if player.checkCollision(block):
                gameOver(gameOver_message,pressAny_message)

            #if player.rect.colliderect(spike.rect1):
            #    print('collision with 1')

            #if player.rect.colliderect(spike.rect2):
            #    print('collision with 2')

            pause_bckgrnd.fill((0, 0, 0, 150))
            pygame.display.update()
            clock.tick(60)

        else:
            surface.blit(pause_bckgrnd,(0,0))
            pause_message.render(surface)
            pause_bckgrnd.fill((0, 0, 0, 0))
            pygame.display.update()
            clock.tick(60)

def gameOver(gameOver_message,pressAny_message):
    gameOver_message.render(surface)
    pressAny_message.render(surface)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    gameLoop()

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue

        return event.key

    return None

gameLoop()

pygame.quit()
quit()