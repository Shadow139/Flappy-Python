from pygame import font
from Color import *
from GameSettings import text_small

__author__ = 'Wiktor'

class Highscore:
    def __init__(self):
        self.score = 0
        self.highscore = self.getHighscore()
        self.highscore_text = text_small.render("Highscore: "+str(self.highscore), True, clr_red)
        self.score_text = text_small.render("Score: "+str(self.score), True, clr_darkgrey)

    def update(self):
        self.score += 1
        print(self.score)

    def render(self,surface):
        self.score_text = text_small.render("Score: "+str(self.score), True, clr_darkgrey)
        if(self.score > self.highscore):
            self.highscore_text = text_small.render("Highscore: "+str(self.score), True, clr_red)

        surface.blit(self.highscore_text,(0,0))
        surface.blit(self.score_text,(0,20))

        
    def getHighscore(self):
        # Default high score
        highscore = 0
     
        # Try to read the high score from a file
        try:
            high_score_file = open("high_score.txt", "r")
            highscore = int(high_score_file.read())
            high_score_file.close()
            print("The high score is", highscore)
        except IOError:
            # Error reading file, no high score
            print("There is no high score yet.")
        except ValueError:
            # There's a file there, but we don't understand the number.
            print("I'm confused. Starting with no high score.")
     
        return highscore
 
 
    def saveHighscore(self,highscore):
        if self.score < self.highscore:
            return

        try:
            # Write the file to disk
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(highscore))
            high_score_file.close()
        except IOError:
            # Hm, can't write it.
            print("Unable to save the high score.")