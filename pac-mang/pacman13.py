# ver 13
# aggiungo la pausa

import random

WIDTH = 700
HEIGHT = 600

t = 0.10
v0 = 200
step = 20

ghost_x = 0
ghost_y = 0
pacman_x = 0
pacman_y = 0
points = 0
v = 0
gameover = False
pause = False

def draw():
    global gameover
    
    screen.fill((0, 0, 0))

    pacman = Actor('pacman')
    pacman.pos = pacman_x, pacman_y
    pacman.draw()

    ghost = Actor('ghost')
    ghost.pos = ghost_x, ghost_y
    ghost.draw()
    
    screen.draw.text("Points: " + str(points), (580, 30), color="white")

    if gameover:
        return
    if ghost_y > pacman_y:
        missed()
    elif pacman.colliderect(ghost):
        eaten()

def reset():
    global pacman_x, pacman_y, ghost_x, ghost_y, points, v, gameover, pause
    
    sounds.chomp.stop()
    sounds.chomp.play(-1)
    ghost_x = random.randint(50, WIDTH-50)
    ghost_y = 0
    pacman_x = WIDTH/2
    pacman_y = HEIGHT-40
    points = 0
    v = v0
    gameover = False
    pause = False

def on_key_down(key):
    global pacman_x, gameover, pause

    if key == keys.R:
        reset()
    if key == keys.P:
        pause_onoff()
    if gameover or pause:
        return
    
    if key == keys.RIGHT and pacman_x < WIDTH:
        pacman_x += step
    elif key == keys.LEFT and pacman_x > 0:
        pacman_x -= step

def eaten():
    global ghost_x, ghost_y, points, v
    
    sounds.eatghost.play()
    ghost_x = random.randint(50, WIDTH-50)
    ghost_y = 0
    points += 1
    v += v0/5

def missed():
    global gameover

    sounds.chomp.stop()
    sounds.death.play()
    gameover = True

def pause_onoff():
    global pause
    
    if pause:
        pause = False
        sounds.chomp.play(-1)
    else:
        pause = True
        sounds.chomp.stop()

def fall():
    global ghost_y, v, gameover

    if gameover or pause:
        return
    ghost_y += v*t


reset()
clock.schedule_interval(fall, t)
