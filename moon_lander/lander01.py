# ver 01
# gioco base, muovo lander con i tasti e vinco se arrivo al suolo

WIDTH = 1000
HEIGHT = 800
player_x = 400
player_y = 150
step = 10

def draw():
    screen.blit('sky', (0, 0))
    
    planet = Actor('ground')
    planet.pos = 0+1000/2, 800-116/2
    planet.draw()
    
    lander = Actor('lander')
    lander.pos = player_x, player_y
    lander.draw()
        
    if lander.colliderect(planet):
        sounds.winner.play()

def on_key_down(key):
    global player_x, player_y, step
    if key == keys.DOWN:
        player_y += step
    elif key == keys.UP:
        player_y -= step
    elif key == keys.RIGHT:
        player_x += step
    elif key == keys.LEFT:
        player_x -= step
