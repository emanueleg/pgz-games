# ver 01
# disegno pacman pronto a mangiare

WIDTH = 700
HEIGHT = 600

pacman_x = WIDTH/2
pacman_y = HEIGHT-40


def draw():
    screen.fill((0, 0, 0))

    pacman = Actor('pacman')
    pacman.pos = pacman_x, pacman_y
    pacman.draw()
