# ver 01
# disegnamo un bel bruco sul prato verde

class Game: pass
game = Game()

WIDTH = 800
HEIGHT = 800
caterpillar = Actor('bruco')

def draw():
    screen.fill((204, 255, 153))
    caterpillar.draw()
