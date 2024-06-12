# ver 06
# facciamo fare "pop" ai palloncini con un click del mouse

import random

class Game: pass
game = Game()

WIDTH = 1000
HEIGHT = 700
game.balloons = []
game.num_balloons = 8
game.colors = ['balloon_red', 'balloon_green', 'balloon_yellow', 'balloon_black', 'balloon_blue']

def draw():
    screen.blit('sky', (0, 0))
    
    for b in game.balloons:
        b.draw()

def reset():
    for i in range(game.num_balloons):
        c = game.colors[random.randint(0, 4)]
        b = Actor(c)
        b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        game.balloons.append(b)

def on_mouse_down(pos):
    for b in game.balloons:
        if b.collidepoint(pos):
            sounds.pop.play()

reset()
