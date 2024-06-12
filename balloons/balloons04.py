# ver 04
# creiamo più di un palloncino giallo nel cielo

import random

class Game: pass
game = Game()

WIDTH = 1000
HEIGHT = 700
game.balloons = []
game.num_balloons = 8

def draw():
    screen.blit('sky', (0, 0))
    
    for b in game.balloons:
        b.draw()


def reset():
    for i in range(game.num_balloons):
        b = Actor('balloon_yellow')
        b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        game.balloons.append(b)

reset()
