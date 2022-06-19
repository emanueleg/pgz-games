# ver 02
# disegniamo un palloncino

WIDTH = 1000
HEIGHT = 700

def draw():
    screen.blit('sky', (0, 0))
    
    baloon = Actor('baloon_red')
    baloon.pos = 100, 100
    baloon.draw()
