__author__ = 'Wiktor'

from random import randint
from ImageLoader import *
from GameSettings import *


class Block:
    def __init__(self, x , y, width, height, min_gap, max_gap,  x_velocity, y_velocity, color):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.width = width
        self.height = height
        self.min_gap = min_gap
        self.max_gap = max_gap
        self.gap = randint(min_gap,max_gap)
        self.color = color

    def update(self):
        self.x -= self.x_velocity

        if self.x < (-1 * self.width):
            self.x = screen_width
            self.height = randint(0,(screen_height/2))
            self.gap = randint(self.min_gap,self.max_gap)

    def renderBlocks(self, surface):
        pygame.draw.rect(surface,self.color,[self.x,self.y,self.width,self.height])
        pygame.draw.rect(surface,self.color,[self.x,self.y + self.height + self.gap,self.width,screen_height])
