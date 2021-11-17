from game.action import Action
from game.point import Point

class HandleOffScreenAction(Action):
    def __init__(self, cast) -> None:
        self._cast = cast

    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                if actor._width == 24:
                    ball = actor
                    ball_position = actor.get_position()
                    if ball_position.is_off_screen_x():
                        ball.bounce("x")
                    if ball_position.is_off_screen_top():
                        ball.bounce("y")
                    if ball_position.is_off_screen_bottom():
                        group.remove(ball)