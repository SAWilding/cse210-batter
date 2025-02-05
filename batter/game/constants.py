import os
from random import randint

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_BRICK = os.path.join(os.getcwd(), f"./cse210-batter/batter/assets/brick-{randint(0, 6)}.png")
IMAGE_PADDLE = os.path.join(os.getcwd(), "./cse210-batter/batter/assets/bat.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./cse210-batter/batter/assets/ball.png")

SOUND_START = os.path.join(os.getcwd(), "./cse210-batter/batter/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./cse210-batter/batter/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./cse210-batter/batter/assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX * -1

PADDLE_X = MAX_X / 2
PADDLE_Y = MAX_Y - 25

BRICK_WIDTH = 48
BRICK_HEIGHT = 24

BRICK_SPACE = 5

PADDLE_SPEED = 15


PADDLE_WIDTH = 96
PADDLE_HEIGHT = 24

BALL_WIDTH = 24
BALL_HEIGHT = 24

SCORE_WIDTH = 50
SCORE_HEIGHT = 25
