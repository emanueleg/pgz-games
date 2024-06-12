# ver 04
# aggiungiamo un contatore di mosse (non si sa mai :-)

class Game: pass
game = Game()

WIDTH = 800
HEIGHT = 800
game.moves = 0
caterpillar = Actor('bruco')
caterpillar.step = 50

def draw():
    screen.fill((204, 255, 153))
    caterpillar.draw()

def on_key_down(key):
    if keyboard.right:
        caterpillar.x += caterpillar.step
        game.moves += 1
    elif keyboard.left:
        caterpillar.x -= caterpillar.step
        game.moves += 1
    elif keyboard.down:
        caterpillar.y += caterpillar.step
        game.moves += 1
    elif keyboard.up:
        caterpillar.y -= caterpillar.step
        game.moves += 1
