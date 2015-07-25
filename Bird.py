__author__ = 'Wiktor'
from ImageLoader import *


class Bird:
    def __init__(self, x , y, x_velocity, y_velocity ,animation):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

        self.animation = animation

        self.rect = self.animation.rect
        self.width = self.rect.width
        self.height = self.rect.height

    def update(self):
        self.y += self.y_velocity

    def render(self,surface):
            self.animation.render(surface,self.x,self.y)

