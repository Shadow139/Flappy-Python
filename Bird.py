__author__ = 'Wiktor'

class Bird:
    """Represents the player.
    Is responsible for tracking players Position, Speed, Animation and Collisions.

    Attributes:
        x,y: Position of the Player. The upper left point of his rectngle.
        x_velocity,y_velocity: Speed in the direction of x and y.
        animation: Is the Animation created with pyganim
        rect: The Rectangle contining the player body inside like a collision box.
        width,height: The width and Height of the player Rectangle.
    """
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
        """
        updates the player Position on each Frame.
        """
        self.y += self.y_velocity

    def render(self,surface):
        """
        renders the player on each Frame.

        :param surface: The surface to render on.

        """
        self.animation.render(surface,self.x,self.y)

    def checkCollision(self,object):
        """
        checks if a Collision ocurred.

        :param object: the object with which the collisoon should be checked.
        :return: A Bool if  collision occuredor not.
        """
        if self.x + self.width > object.x:
            if self.x < object.x + object.width:
                if self.y < object.height:
                    if(self.x - self.width < object.x + object.width):
                        return True

        if self.x + self.width > object.x:
            if self.y + self.height -20 > object.height + object.gap:
                if self.x < object.x + object.width:
                    return True

        return False