# ver 03
# muovo pacman

WIDTH = 700
HEIGHT = 600

step = 20

pacman_x = WIDTH/2
pacman_y = HEIGHT-40


def draw():
    screen.fill((0, 0, 0))

    pacman = Actor('pacman')
    pacman.pos = pacman_x, pacman_y
    pacman.draw()


def on_key_down(key):
    global pacman_x

    if key == keys.RIGHT:
        pacman_x += step
    elif key == keys.LEFT:
        pacman_x -= step

sounds.chomp.play(-1)
