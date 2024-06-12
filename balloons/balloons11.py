# ver 11
# quando scade il tempo non posso più fare nulla

import random

class Game: pass
game = Game()

WIDTH = 1000
HEIGHT = 700
game.balloons = []
game.num_balloons = 8
game.colors = ['balloon_red', 'balloon_green', 'balloon_yellow', 'balloon_black', 'balloon_blue']
game.points = 0
game.GAMETIME = 60
game.time = 0
game.gameover = False

def draw():
    screen.blit('sky', (0, 0))
    
    for b in game.balloons:
        b.draw()
    
    screen.draw.text("Punti: " + str(game.points), (800, 40), color="white", shadow=(1.0,1.0), scolor="black", fontsize=38)
    screen.draw.text("Tempo: " + str(game.time), (600, 40), color="white", shadow=(1.0,1.0), scolor="black", fontsize=38)

def reset():
    for i in range(game.num_balloons):
        c = game.colors[random.randint(0, 4)]
        b = Actor(c)
        b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        game.balloons.append(b)
    game.points = 0
    game.time = game.GAMETIME
    game.gameover = False

def timer():
    if game.time > 0:
        game.time -= 1
    else: 
        game.gameover = True

def on_mouse_down(pos):
    if game.gameover:
        return
    for b in game.balloons:
        if b.collidepoint(pos):
            b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            b.image = game.colors[random.randint(0, 4)]
            sounds.pop.play()
            game.points += 1
            break

reset()
clock.schedule_interval(timer, 1)
