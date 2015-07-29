__author__ = 'Wiktor'

"""
A Class contining Functions for Image Loading,Scaling and Clipping.
"""

import pygame

def imageLoaderScaledAndClipped(image, scale, clip):
    asset = pygame.image.load(image)
    playerClipped = pygame.Surface( (clip[2],clip[3]) )
    playerClipped.blit(asset, (0,0), clip)
    #scaledAsset = (clip[2] * scale, clip[3] * scale)
    scaledAsset = pygame.transform.scale(playerClipped, (clip[2] * scale, clip[3] * scale))

    return scaledAsset

def imageLoaderScaled(image,scale):
    asset = pygame.image.load(image)
    rect = asset.get_rect()
    scale_x = int(rect.width * scale)
    scale_y = int(rect.height * scale)
    scaledAsset = pygame.transform.scale(asset, (scale_x, scale_y))

    return scaledAsset

def imageLoaderPixelScaled(image,scale_x,scale_y):
    asset = pygame.image.load(image)
    rect = asset.get_rect()
    scaledAsset = pygame.transform.scale(asset, (scale_x, scale_y))

    return scaledAsset

def imageLoader(image):
    asset = pygame.image.load(image)


    return asset