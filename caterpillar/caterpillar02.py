# ver 02
# facciamo muovere a destra il bruco con la freccetta

class Game: pass
game = Game()

WIDTH = 800
HEIGHT = 800
caterpillar = Actor('bruco')
caterpillar.step = 50

def draw():
    screen.fill((204, 255, 153))
    caterpillar.draw()

def on_key_down(key):
    if keyboard.right:
        caterpillar.x += caterpillar.step
