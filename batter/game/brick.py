from game.actor import Actor
from game.point import Point
from game import constants
from random import randint
import os

class Brick(Actor):
    def __init__(self, x, y):
        super().__init__()
        self.prepare(x, y)

    def prepare(self, x, y):
        self.set_image(os.path.join(os.getcwd(), f"./cse210-batter/batter/assets/brick-{randint(0, 6)}.png"))
        self.set_height(constants.BRICK_HEIGHT)
        self.set_width(constants.BRICK_WIDTH)
        self.set_position(Point(x, y))

