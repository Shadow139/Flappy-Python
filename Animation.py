import os
import pyganim

__author__ = 'Wiktor'

from ImageLoader import *

class Animation:
    def __init__(self,frames, scale, frametime):
        self.anim_frames = []

        for file in os.listdir(frames):
            if file.endswith(".png"):
                self.anim_frames.append((imageLoaderScaled(str(frames + file),scale),frametime))

        self.rect = self.anim_frames[0][0].get_rect()

        self.animation = pyganim.PygAnimation(self.anim_frames)
        self.animation.play()


    def render(self,surface,x,y):
        self.animation.blit(surface,(x,y))
