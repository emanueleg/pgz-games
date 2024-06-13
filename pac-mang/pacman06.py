# ver 06
# posizione casualmente il fantasma in alto

import random

class Game: pass
game = Game()

WIDTH = 700
HEIGHT = 600

pacman = Actor('pacman')
ghost = Actor('ghost')

pacman.x = WIDTH/2
pacman.y = HEIGHT-40
pacman.step = 10

ghost.x = random.randint(50, WIDTH-50)
ghost.y = 0
ghost.v = 0


def draw():
    screen.fill((0, 0, 0))
    pacman.draw()
    ghost.draw()

def update():
    if keyboard.right and pacman.x < WIDTH:
        pacman.x += pacman.step
    elif keyboard.left and pacman.x > 0:
        pacman.x -= pacman.step

sounds.chomp.play(-1)
