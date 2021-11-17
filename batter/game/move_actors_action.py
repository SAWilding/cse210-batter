from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    def __init__(self, cast):
        self._cast = cast

    def execute(self, cast):
        for group in cast.values():
            for i in range(len(group)):
                position = group[i].get_position()
                x_position = position.get_x()
                y_position = position.get_y()

                velocity = group[i].get_velocity()
                x_velocity = velocity.get_x()
                y_velocity = velocity.get_y()

                group[i].set_position(Point(x_position + x_velocity, y_position + y_velocity))