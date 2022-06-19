# ver 11
# quando scade il tempo non posso più fare nulla

import random

WIDTH = 1000
HEIGHT = 700
baloons = []
num_baloons = 8
colors = ['baloon_red', 'baloon_green', 'baloon_yellow', 'baloon_black', 'baloon_blue']
points = 0
GAMETIME = 60
time = 0
gameover = False

def draw():
    screen.blit('sky', (0, 0))
    
    for b in baloons:
        b.draw()
    
    screen.draw.text("Punti: " + str(points), (800, 40), color="white", shadow=(1.0,1.0), scolor="black", fontsize=38)
    screen.draw.text("Tempo: " + str(time), (600, 40), color="white", shadow=(1.0,1.0), scolor="black", fontsize=38)

def reset():
    global baloons, num_baloons, points, time, gameover
    
    for i in range(num_baloons):
        c = colors[random.randint(0, 4)]
        b = Actor(c)
        b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        baloons.append(b)
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
    global baloons, points, gameover
    if gameover:
        return
    for b in baloons:
        if b.collidepoint(pos):
            b.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            b.image = colors[random.randint(0, 4)]
            sounds.pop.play()
            points += 1
            break

reset()
clock.schedule_interval(timer, 1)
