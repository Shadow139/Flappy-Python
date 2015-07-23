__author__ = 'Wiktor'

import pygame

clr_black = (0,0,0)
clr_white = (255,255,255)


pygame.init()

surface = pygame.display.set_mode((800,600))

pygame.display.set_caption("Awaaaysomeee Game!")

clock = pygame.time.Clock()

def bird(x,y,image):
    surface.blit(image,(x,y))

img = pygame.image.load('Assets/bird.png')
bird_x = 150
bird_y = 200


game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    surface.fill(clr_black)
    bird(bird_x,bird_y,img)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()