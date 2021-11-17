from game.action import Action
from game import constants
from game.point import Point

class HandleCollisionsAction(Action):
    def __init__(self, physics_service, audio_service, scoreboard) -> None:
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._scoreboard = scoreboard
    def execute(self, cast):
        balls = []
        bricks = []
        for group in cast.values():
            for actor in group:
                if actor.get_width() == constants.PADDLE_WIDTH:
                    paddle = actor
                if actor.get_width() == constants.BALL_WIDTH:
                    balls.append(actor)
                    ball_group = group
                if actor.get_width() == constants.BRICK_WIDTH:
                    bricks.append(actor)
                    brick_group = group
                    
        
        if balls != []:
            for ball in balls:
                if self._physics_service.is_collision(paddle, ball):
                    self._audio_service.play_sound(constants.SOUND_BOUNCE)
                    ball.bounce("y")
            for brick in bricks:
                if self._physics_service.is_collision(brick, ball):
                    self._audio_service.play_sound(constants.SOUND_BOUNCE)
                    ball.bounce("y")
                    brick_group.remove(brick)
                    self._scoreboard.add_points(1)
        

