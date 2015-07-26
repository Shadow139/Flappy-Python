__author__ = 'Wiktor'

class MessageOnScreen:
    def __init__(self,message,center_x,center_y,font,color):
        self.message= message
        self.center_x = center_x
        self.center_y = center_y
        self.font = font

        self.text = self.font.render(self.message,True,color)
        self.rect = self.text.get_rect()

        self.rect.center = (center_x,center_y)

    def render(self,surface):
        surface.blit(self.text,self.rect)