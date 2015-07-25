__author__ = 'Wiktor'

from ImageLoader import *


class Spike:
    def __init__(self, x , y, width, height, gap, x_velocity, y_velocity, image,image_flipped):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gap = gap

        self.asset = imageLoaderPixelScaled(image,width,300)
        self.asset_flipped = imageLoaderPixelScaled(image_flipped,width, 300)

        self.rect1 = self.asset.get_rect()
        self.rect2 = self.asset_flipped.get_rect()

        print(self.asset.get_rect())
        print(self.asset_flipped.get_rect())

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity


    def renderBlocks(self, surface,screen_height):
        surface.blit(self.asset_flipped,(self.x,self.height - 300))
        self.rect1.topleft = (self.x,self.height - 300)
        surface.blit(self.asset,(self.x,self.height + self.gap))
        self.rect2.topleft = (self.x,self.height + self.gap)
