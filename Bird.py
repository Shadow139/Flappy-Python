__author__ = 'Wiktor'
from ImageLoader import *


class Bird:
    def __init__(self, x , y, x_velocity, y_velocity, image):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

        self.asset = imageLoader(image)
        self.rect = self.asset.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
