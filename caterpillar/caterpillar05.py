# ver 05
# all'avvio il bruco è in posizione casuale

import random

class Game: pass
game = Game()

WIDTH = 800
HEIGHT = 800
game.moves = 0
caterpillar = Actor('bruco')
caterpillar.step = 50

def draw():
    screen.fill((204, 255, 153))
    caterpillar.draw()

def setup(): 
    caterpillar.x = random.randint(0, WIDTH)
    caterpillar.y = random.randint(0, HEIGHT)

def on_key_down(key):
    if keyboard.right:
        caterpillar.x += caterpillar.step
        game.moves += 1
    elif keyboard.left:
        caterpillar.x -= caterpillar.step
        game.moves += 1
    elif keyboard.down:
        caterpillar.y += caterpillar.step
        game.moves += 1
    elif keyboard.up:
        caterpillar.y -= caterpillar.step
        game.moves += 1

setup()