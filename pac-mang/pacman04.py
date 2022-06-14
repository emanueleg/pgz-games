# ver 04
# muovo pacman fermandomi ai bordi dx e sx dello schermo

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

    if key == keys.RIGHT and pacman_x < WIDTH:
        pacman_x += step
    elif key == keys.LEFT and pacman_x > 0:
        pacman_x -= step

sounds.chomp.play(-1)
