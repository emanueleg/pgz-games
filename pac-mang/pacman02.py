# ver 02
# aggiungo un suono in background

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

sounds.chomp.play(-1)
