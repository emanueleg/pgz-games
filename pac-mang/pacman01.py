# ver 01
# disegno pacman pronto a mangiare

class Game: pass
game = Game()

WIDTH = 700
HEIGHT = 600

pacman = Actor('pacman')
pacman.x = WIDTH/2
pacman.y = HEIGHT-40


def draw():
    screen.fill((0, 0, 0))
    pacman.draw()
