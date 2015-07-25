__author__ = 'Wiktor'
from ImageLoader import *


class Background:
    def __init__(self,image,x,y):
        self.x = x
        self.y = y
        self.asset = imageLoader(image)


    def render(self,surface,screen_width):
        surface.blit(self.asset, (self.x,self.y))
