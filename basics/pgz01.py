class Game: pass
game = Game()

RED = 150, 0, 0
GREEN = 0, 128, 0

game.bg = RED

def draw():
    screen.fill(game.bg)

def on_mouse_down():
    game.bg = GREEN

def on_mouse_up():
    game.bg = RED
