# ver 04
# creiamo più di un palloncino giallo nel cielo

import random

WIDTH = 1000
HEIGHT = 700
balloons = []
num_balloons = 8

def draw():
    screen.blit('sky', (0, 0))
    
    for b in balloons:
        b.draw()


def reset():
    global balloons, num_balloons
    for i in range(num_balloons):
        b = Actor('balloon_yellow')
        b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        balloons.append(b)

reset()
