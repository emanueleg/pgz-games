# ver 05
# mostro uso carburante e velocità

WIDTH = 1000
HEIGHT = 800
player_x = 400
player_y = 150
landed = False
step = 5
t = 0.10

a = 15
v0 = 0
fuel = 100

def draw():
    global landed
    screen.blit('sky', (0, 0))
    
    planet = Actor('ground')
    planet.pos = 500, 742
    planet.draw()
    
    lander = Actor('lander')
    lander.pos = player_x, player_y
    lander.draw()
    
    screen.draw.text("Fuel: " + str(fuel), (780, 30), color="white")
    screen.draw.text("Speed: " + str(v0), (870, 30), color="white")
    
    if lander.colliderect(planet):
        if not landed:
            sounds.winner.play()
            landed = True

def reset():
    global player_x, player_y, landed
    landed = False
    player_x = 400
    player_y = 150
    a = 15
    v0 = 0

def on_key_down(key):
    global player_x, player_y, step, winner
    
    if key == keys.R:
        reset()
    if landed:
        return
    
    if key == keys.UP:
        decelerate()
    elif key == keys.RIGHT:
        player_x += step
    elif key == keys.LEFT:
        player_x -= step

def decelerate():
    global player_y, v0, t, a, winner, fuel
    if fuel <= 0:
        return
    a1 = -2 * a
    v = v0 + a1*t
    s = 0.5*a1*t + v*t
    player_y += s
    v0 = v
    fuel -= 1

def gravity():
    global player_y, v0, a, t, winner
    if landed:
        return
    v = v0 + a*t
    s = 0.5*a*t + v*t
    player_y += s
    v0 = v

clock.schedule_interval(gravity, t)
