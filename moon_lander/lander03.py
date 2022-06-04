# ver 03
# implemento il reset per ricominciare

WIDTH = 1000
HEIGHT = 800
player_x = 400
player_y = 150
step = 50
landed = False

def draw():
    global landed
    screen.blit('sky', (0, 0))
    
    planet = Actor('ground')
    planet.pos = 500, 742
    planet.draw()
    
    lander = Actor('lander')
    lander.pos = player_x, player_y
    lander.draw()
        
    if lander.colliderect(planet):
        sounds.winner.play()
        landed = True

def reset():
    global player_x, player_y, landed
    landed = False
    player_x = 400
    player_y = 150

def on_key_down(key):
    global player_x, player_y, step, landed
    
    if key == keys.R:
        reset()
    if landed:
        return
    
    if key == keys.DOWN:
        player_y += step
    elif key == keys.UP:
        player_y -= step
    elif key == keys.RIGHT:
        player_x += step
    elif key == keys.LEFT:
        player_x -= step
