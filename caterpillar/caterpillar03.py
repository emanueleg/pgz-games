# ver 03
# facciamo muovere il bruco con le freccette con un buon passo

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
    elif keyboard.left:
        caterpillar.x -= caterpillar.step
    elif keyboard.down:
        caterpillar.y += caterpillar.step
    elif keyboard.up:
        caterpillar.y -= caterpillar.step
