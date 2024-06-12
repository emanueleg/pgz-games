# ver 13
# aggiungo la pausa

import random

class Game: pass
game = Game()

WIDTH = 700
HEIGHT = 600

game.t = 0.10
game.v0 = 200

pacman = Actor('pacman')
ghost = Actor('ghost')

ghost.v = 0
pacman.step = 10

game.points = 0
game.gameover = False
game.pause = False


def draw():
    screen.fill((0, 0, 0))
    pacman.draw()
    ghost.draw()
    
    screen.draw.text("points: " + str(game.points), (580, 30), color="white")

def update():
    if game.gameover or game.pause:
        return    
    if ghost.y > pacman.y:
        missed()
    elif pacman.colliderect(ghost):
        eaten()
    if keyboard.right and pacman.x < WIDTH:
        pacman.x += pacman.step
    elif keyboard.left and pacman.x > 0:
        pacman.x -= pacman.step

def reset():
    sounds.chomp.stop()
    sounds.chomp.play(-1)
    ghost.x = random.randint(50, WIDTH-50)
    ghost.y = 0
    pacman.x = WIDTH/2
    pacman.y = HEIGHT-40
    game.points = 0
    ghost.v = game.v0
    game.gameover = False
    game.pause = False

def on_key_down(key):
    if key == keys.R:
        reset()
    if key == keys.P:
        game.pause_onoff()
    if game.gameover or game.pause:
        return

def eaten():
    sounds.eatghost.play()
    game.points += 1
    ghost.x = random.randint(50, WIDTH-50)
    ghost.y = 0
    ghost.v += game.v0/5

def missed():
    sounds.chomp.stop()
    sounds.death.play()
    game.gameover = True

def pause_onoff():
    if game.pause:
        game.pause = False
        sounds.chomp.play(-1)
    else:
        game.pause = True
        sounds.chomp.stop()

def fall():
    if game.gameover or game.pause:
        return
    ghost.y += ghost.v*game.t

reset()
clock.schedule_interval(fall, game.t)
