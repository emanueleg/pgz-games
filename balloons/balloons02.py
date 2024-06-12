# ver 02
# disegniamo un palloncino

class Game: pass
game = Game()

WIDTH = 1000
HEIGHT = 700

def draw():
    screen.blit('sky', (0, 0))
    
    balloon = Actor('balloon_red')
    balloon.pos = 100, 100
    balloon.draw()
