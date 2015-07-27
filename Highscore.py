from pygame import font
from Color import clr_darkgrey
from GameSettings import text_small

__author__ = 'Wiktor'

class Highscore:
    def __init__(self):
        self.score = 0
        self.text = text_small.render("Score: "+str(self.score), True, clr_darkgrey)


    def update(self):
        self.score += 1

    def render(self,surface):
        self.text = text_small.render("Score: "+str(self.score), True, clr_darkgrey)
        surface.blit(self.text,(0,0))