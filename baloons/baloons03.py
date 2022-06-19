# ver 03
# posizioniamo casualmente il palloncino

import random

WIDTH = 1000
HEIGHT = 700

def draw():
    screen.blit('sky', (0, 0))
    
    baloon = Actor('baloon_red')
    baloon.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    baloon.draw()
