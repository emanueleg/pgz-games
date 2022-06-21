# ver 01
# al via, muoviamo la palla verso una direzione casuale (in radianti)

import random
import math

WIDTH = 600
HEIGHT = 600
BALL_RADIUS = images.ball.get_width()//2

ball = Actor('ball')
ball.pos = WIDTH//2, HEIGHT//2
ball.dir = random.uniform(0, 2*math.pi)
t = 0.025
v = 200

def draw():   
    screen.fill((0, 180, 0))
    screen.draw.line((0, HEIGHT//2), (WIDTH, HEIGHT//2), (255, 255, 255))
    screen.draw.circle((WIDTH//2, HEIGHT//2), 100, (255, 255, 255))
    screen.draw.filled_circle((WIDTH//2, HEIGHT//2), 5, (255, 255, 255))
    ball.draw()

def move():
    global ball

    x,y = ball.pos
    x1 = x + int(math.cos(ball.dir)*t*v)
    y1 = y + int(math.sin(ball.dir)*t*v)
    ball.pos = x1, y1

clock.schedule_interval(move, t)
