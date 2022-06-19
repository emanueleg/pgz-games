# ver 06
# facciamo fare "pop" ai palloncini con un click del mouse

import random

WIDTH = 1000
HEIGHT = 700
baloons = []
num_baloons = 8
colors = ['baloon_red', 'baloon_green', 'baloon_yellow', 'baloon_black', 'baloon_blue']

def draw():
    screen.blit('sky', (0, 0))
    
    for b in baloons:
        b.draw()

def reset():
    global baloons, num_baloons
    for i in range(num_baloons):
        c = colors[random.randint(0, 4)]
        b = Actor(c)
        b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        baloons.append(b)

def on_mouse_down(pos):
    global baloons
    for b in baloons:
        if b.collidepoint(pos):
            sounds.pop.play()

reset()
