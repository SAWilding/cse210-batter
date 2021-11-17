from game.actor import Actor
from game import constants
from game.point import Point

class Ball(Actor):
    def __init__(self):
        super().__init__()
        self.prepare()

    def prepare(self):
        self.set_position(Point((constants.BALL_X), (constants.BALL_Y)))
        self.set_height(constants.BALL_HEIGHT)
        self.set_width(constants.BALL_WIDTH)
        self.set_image(constants.IMAGE_BALL)
        self.set_velocity(Point(constants.BALL_DX, constants.BALL_DY))

    def bounce(self, axis):
        if axis == "x":
            x_velocity = self.get_velocity().get_x() * -1
            y_velocity = self.get_velocity().get_y()
            self.set_velocity(Point(x_velocity, y_velocity))
        elif axis == "y":
            x_velocity = self.get_velocity().get_x()
            y_velocity = self.get_velocity().get_y() * -1
            self.set_velocity(Point(x_velocity, y_velocity))
