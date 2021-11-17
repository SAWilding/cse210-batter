from game.action import Action
from game import constants
from game.point import Point

class ControlActorsAction(Action):
    def __init__(self, input_service) -> None:
        self._input_service = input_service

    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                if actor.get_width() == constants.PADDLE_WIDTH:
                    paddle = actor
                    if self._input_service.is_left_pressed():
                        paddle.set_velocity(Point(-constants.PADDLE_SPEED, 0))
                    elif self._input_service.is_right_pressed():
                        paddle.set_velocity(Point(constants.PADDLE_SPEED, 0))
                    else:
                        paddle.set_velocity(Point(0, 0))