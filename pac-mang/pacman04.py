# ver 04
# muovo pacman fermandomi ai bordi dx e sx dello schermo

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
    if keyboard.right and pacman.x < WIDTH:
        pacman.x += pacman.step
    elif keyboard.left and pacman.x > 0:
        pacman.x -= pacman.step

sounds.chomp.play(-1)
