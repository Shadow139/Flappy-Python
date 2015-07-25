__author__ = 'Wiktor'

class ParallaxScrolling:
    def __init__(self,graphic1,graphic2,scrollspeed):
        self.graphic1 = graphic1
        self.graphic2 = graphic2
        self.scrollspeed = scrollspeed

    def render(self,surface,scroll_length):
        surface.blit(self.graphic1.asset, (self.graphic1.x, self.graphic1.y))
        surface.blit(self.graphic2.asset, (self.graphic2.x, self.graphic2.y))

        self.graphic1.x = self.graphic1.x + self.scrollspeed
        self.graphic2.x = self.graphic2.x + self.scrollspeed

        if self.graphic1.x <= -scroll_length:
            self.graphic1.x = scroll_length - 1

        if self.graphic2.x <= -scroll_length:
            self.graphic2.x = scroll_length - 1