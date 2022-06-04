# ver 06
# coloro velocità e carburante e determino se vinco o perdo

WIDTH = 1000
HEIGHT = 800
player_x = 400
player_y = 150
max_speed = 20.0
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
    
    if fuel <= 0:
        screen.draw.text("Fuel: " + str(fuel), (780, 30), color="red")
    else:
        screen.draw.text("Fuel: " + str(fuel), (780, 30), color="white")
        
    if v0 <= max_speed:
        screen.draw.text("Speed: " + str(v0), (870, 30), color="white")
    else:
        screen.draw.text("Speed: " + str(v0), (870, 30), color="red")
    
    if lander.colliderect(planet):
        if not landed:
            landed = True
            if v0 <= max_speed:
                sounds.winner.play()
            else:
                sounds.loser.play()

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
