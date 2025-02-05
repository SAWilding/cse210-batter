import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction
from game.scoreboard import Scoreboard
def create_bricks():
    bricks = []
    for y in range(10, 200, constants.BRICK_HEIGHT + 25):
        for x in range(10, 800 - constants.BRICK_WIDTH, constants.BRICK_WIDTH + 25):
            bricks.append(Brick(x, y))
    print(bricks)
    return bricks

def main():

    # create the cast {key: tag, value: list}
    cast = {}
    scoreboard = Scoreboard()
    bricks = create_bricks()
    cast["bricks"] = bricks
    # TODO: Create bricks here and add them to the list

    cast["balls"] = [Ball()]
    # TODO: Create a ball here and add it to the list

    cast["paddle"] = [Paddle()]
    # TODO: Create a paddle here and add it to the list
    cast["scoreboard"] = [scoreboard]

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction(cast)
    handle_off_screen_action = HandleOffScreenAction(cast)
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service, audio_service, scoreboard)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action, handle_off_screen_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()
    audio_service.play_sound(constants.SOUND_OVER)
    audio_service.stop_audio()

if __name__ == "__main__":
    main()
