# ver 04
# creiamo più di un palloncino giallo nel cielo

import random

WIDTH = 1000
HEIGHT = 700
baloons = []
num_baloons = 8

def draw():
    screen.blit('sky', (0, 0))
    
    for b in baloons:
        b.draw()


def reset():
    global baloons, num_baloons
    for i in range(num_baloons):
        b = Actor('baloon_yellow')
        b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        baloons.append(b)

reset()
