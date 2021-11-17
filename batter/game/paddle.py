from game.actor import Actor
from game import constants
from game.point import Point

class Paddle(Actor):
    def __init__(self) -> None:
        super().__init__()
        self._prepare()

    def _prepare(self):
        self.set_image(constants.IMAGE_PADDLE)
        self.set_width(constants.PADDLE_WIDTH)
        self.set_height(constants.PADDLE_HEIGHT)
        self.set_position(Point(constants.PADDLE_X, constants.PADDLE_Y))