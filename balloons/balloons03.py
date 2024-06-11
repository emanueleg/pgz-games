# ver 03
# posizioniamo casualmente il palloncino

import random

WIDTH = 1000
HEIGHT = 700

def draw():
    screen.blit('sky', (0, 0))
    
    balloon = Actor('balloon_red')
    balloon.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    balloon.draw()
