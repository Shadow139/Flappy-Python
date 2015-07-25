__author__ = 'Wiktor'

from ImageLoader import *
from GameSettings import *
from random import randint
from Color import clr_black

class Spike:
    def __init__(self, x , y, width, height, gap, x_velocity, y_velocity, image,image_flipped):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gap = gap

        self.x_flipped = x
        self.y_flipped = height + gap
        self.width_flipped = width
        self.height_flipped = screen_height - (height + gap)

        self.asset = imageLoaderPixelScaled(image,width,300)
        self.asset_flipped = imageLoaderPixelScaled(image_flipped,width, 300)

        self.rect1 = pygame.Rect(self.x,self.height - 300,self.width,300)
        self.rect2 = pygame.Rect(self.x_flipped,self.y_flipped,self.width_flipped,300)

        print(self.rect1)
        print(self.rect2)

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def update(self):
        self.x -= self.x_velocity
        self.x_flipped =self.x
        self.rect1.x = self.x
        self.rect2.x = self.x_flipped

        if self.x < (-1 * self.width):
            self.x = screen_width
            self.height = randint(0,screen_height/2)
            self.updateRects()

    def updateRects(self):
        self.y_flipped = self.height + self.gap

        self.rect1 = pygame.Rect(self.x,self.height - 300,self.width,300)
        self.rect2 = pygame.Rect(self.x_flipped,self.y_flipped,self.width_flipped,300)

    def render(self, surface):
        #print("Paint Upper: x: " + str(self.x) + " y: " + str(self.height - 300) )
       # print("Paint Lower: x: " + str(self.x) + " y: " + str(self.height + self.gap))

        #print("Rect Upper: x: " + str(self.rect1.x) + " y: " + str(self.rect1.y))
        #print("Rect Lower: x: " + str(self.rect2.x) + " y: " + str(self.rect2.y))

        surface.blit(self.asset_flipped,(self.x,self.height - 300))
        surface.blit(self.asset,(self.x,self.height + self.gap))
        pygame.draw.rect(surface,clr_black,self.rect1)
        pygame.draw.rect(surface,clr_black,self.rect2)