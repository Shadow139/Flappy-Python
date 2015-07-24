__author__ = 'Wiktor'

from ImageLoader import *


class Block:
    def __init__(self, x , y, width, height, gap, x_velocity, y_velocity, color):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.width = width
        self.height = height
        self.gap = gap
        self.color = color

    def renderBlocks(self, surface,screen_height):
        pygame.draw.rect(surface,self.color,[self.x,self.y,self.width,self.height])
        pygame.draw.rect(surface,self.color,[self.x,self.y + self.height + self.gap,self.width,screen_height])
