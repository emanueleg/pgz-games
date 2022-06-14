# ver 07
# faccio cadere il fantasma

import random

WIDTH = 700
HEIGHT = 600

t = 0.10
v0 = 200
step = 20

ghost_x = random.randint(50, WIDTH-50)
ghost_y = 0
pacman_x = WIDTH/2
pacman_y = HEIGHT-40


def draw():
    screen.fill((0, 0, 0))

    pacman = Actor('pacman')
    pacman.pos = pacman_x, pacman_y
    pacman.draw()

    ghost = Actor('ghost')
    ghost.pos = ghost_x, ghost_y
    ghost.draw()


def on_key_down(key):
    global pacman_x

    if key == keys.RIGHT and pacman_x < WIDTH:
        pacman_x += step
    elif key == keys.LEFT and pacman_x > 0:
        pacman_x -= step

def fall():
    global ghost_y, v0
    ghost_y += v0*t


sounds.chomp.play(-1)
clock.schedule_interval(fall, t)
