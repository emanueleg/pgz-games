# ver 07
# il palloncino esploso sparisce e ne compare un'altro altrove

import random

WIDTH = 1000
HEIGHT = 700
balloons = []
num_balloons = 8
colors = ['balloon_red', 'balloon_green', 'balloon_yellow', 'balloon_black', 'balloon_blue']

def draw():
    screen.blit('sky', (0, 0))
    
    for b in balloons:
        b.draw()

def reset():
    global balloons, num_balloons
    for i in range(num_balloons):
        c = colors[random.randint(0, 4)]
        b = Actor(c)
        b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        balloons.append(b)

def on_mouse_down(pos):
    global balloons
    for b in balloons:
        if b.collidepoint(pos):
            b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            b.image = colors[random.randint(0, 4)]
            sounds.pop.play()

reset()
