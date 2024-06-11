# ver 11
# quando scade il tempo non posso più fare nulla

import random

WIDTH = 1000
HEIGHT = 700
balloons = []
num_balloons = 8
colors = ['balloon_red', 'balloon_green', 'balloon_yellow', 'balloon_black', 'balloon_blue']
points = 0
GAMETIME = 60
time = 0
gameover = False

def draw():
    screen.blit('sky', (0, 0))
    
    for b in balloons:
        b.draw()
    
    screen.draw.text("Punti: " + str(points), (800, 40), color="white", shadow=(1.0,1.0), scolor="black", fontsize=38)
    screen.draw.text("Tempo: " + str(time), (600, 40), color="white", shadow=(1.0,1.0), scolor="black", fontsize=38)

def reset():
    global balloons, num_balloons, points, time, gameover
    
    for i in range(num_balloons):
        c = colors[random.randint(0, 4)]
        b = Actor(c)
        b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        balloons.append(b)
    points = 0
    time = GAMETIME
    gameover = False

def timer():
    global time, gameover
    
    if time > 0:
        time -= 1
    else:    
        gameover = True

def on_mouse_down(pos):
    global balloons, points, gameover
    if gameover:
        return
    for b in balloons:
        if b.collidepoint(pos):
            b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            b.image = colors[random.randint(0, 4)]
            sounds.pop.play()
            points += 1
            break

reset()
clock.schedule_interval(timer, 1)
