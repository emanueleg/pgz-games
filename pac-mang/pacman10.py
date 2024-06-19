# ver 10
# contiamo i fantasmi mangiati

import random

class Game: pass
game = Game()

WIDTH = 700
HEIGHT = 600

game.t = 0.10
game.v0 = 200

pacman = Actor('pacman')
ghost = Actor('ghost')

pacman.step = 10
ghost.v = 0

game.points = 0

def draw():
    screen.fill((0, 0, 0))
    pacman.draw()
    ghost.draw()
    screen.draw.text("Points: " + str(game.points), (580, 30), color="white")

def update():
    if ghost.y > pacman.y:
        miss()
    elif pacman.colliderect(ghost):
        eat()
    if keyboard.right and pacman.x < WIDTH:
        pacman.x += pacman.step
    elif keyboard.left and pacman.x > 0:
        pacman.x -= pacman.step

def reset():
    sounds.chomp.stop()
    sounds.chomp.play(-1)
    ghost.x = random.randint(50, WIDTH-50)
    ghost.y = 0
    ghost.v = game.v0
    pacman.x = WIDTH/2
    pacman.y = HEIGHT-40
    game.points = 0

def on_key_down(key):
    if key == keys.R:
        reset()

def eat():
    sounds.eatghost.play()
    ghost.x = random.randint(50, WIDTH-50)
    ghost.y = 0
    game.points += 1

def miss():
    sounds.death.play()
    ghost.x = random.randint(50, WIDTH-50)
    ghost.y = 0

def fall():
    ghost.y += ghost.v*game.t

reset()
clock.schedule_interval(fall, game.t)
