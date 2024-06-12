# ver 09
# e il bruco vola via

import random

class Game: pass
game = Game()

WIDTH = 800
HEIGHT = 800
game.moves = 0
caterpillar = Actor('bruco')
apple = Actor('mela')
caterpillar.step = 50
apple.timer = 5

def draw():
    screen.fill((204, 255, 153))
    if caterpillar.colliderect(apple):
        apple.image = 'mela_morso'
        caterpillar.image = 'farfalla'
        caterpillar.draw()
        clock.unschedule(move_apple)
        animate(caterpillar, pos=(-200, -200))
    else:
        apple.draw()
        caterpillar.draw()        

def setup(): 
    apple.x = random.randint(0, WIDTH)
    apple.y = random.randint(0, HEIGHT)
    caterpillar.x = random.randint(0, WIDTH)
    caterpillar.y = random.randint(0, HEIGHT)

def move_apple():
    apple.x = random.randint(0, WIDTH)
    apple.y = random.randint(0, HEIGHT)

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
clock.schedule_interval(move_apple, apple.timer)
