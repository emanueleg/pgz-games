# ver 03
# muovo pacman

class Game: pass
game = Game()

WIDTH = 700
HEIGHT = 600

pacman = Actor('pacman')
pacman.x = WIDTH/2
pacman.y = HEIGHT-40
pacman.step = 10


def draw():
    screen.fill((0, 0, 0))
    pacman.draw()

def update():
    if keyboard.right:
        pacman.x += pacman.step
    elif keyboard.left:
        pacman.x -= pacman.step

sounds.chomp.play(-1)
