__author__ = 'Wiktor'

import pygame

clr_black = (0,0,0)
clr_white = (255,255,255)

screen_width = 800
screen_height = 600

pygame.init()

surface = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Awaaaysomeee Game!")

clock = pygame.time.Clock()

def gameOver():
    pygame.quit()
    quit()

def bird(x,y,image):
    surface.blit(image,(x,y))

img = pygame.image.load('Assets/bird.png')
bird_x = 150
bird_y = 200

bird_y_move = 5


game_over = False

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

    if bird_y > screen_height - 40 or bird_y < 0 :
        gameOver()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()