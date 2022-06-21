# ver 01
# disegnamo il campo e la palla al centro

import random
import math

WIDTH = 600
HEIGHT = 600
BALL_RADIUS = images.ball.get_width()//2

ball = Actor('ball')
ball.pos = WIDTH//2, HEIGHT//2

def draw():   
    screen.fill((0, 180, 0))
    screen.draw.line((0, HEIGHT//2), (WIDTH, HEIGHT//2), (255, 255, 255))
    screen.draw.circle((WIDTH//2, HEIGHT//2), 100, (255, 255, 255))
    screen.draw.filled_circle((WIDTH//2, HEIGHT//2), 5, (255, 255, 255))
    ball.draw()
