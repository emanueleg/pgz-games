# ver 04
# un po' di trigonometria

import math

WIDTH = 600
HEIGHT = 700

mouse_x = 0
mouse_y = 0

def draw():
    global mouse_x, mouse_y
    screen.blit('minion_01', (0, 0))

    eye_x = 288
    eye_y = 182
    eye_r = 77
    pupil_r = 25

    distance_x = mouse_x - eye_x
    distance_y = mouse_y - eye_y
    distance = math.sqrt(distance_x**2 + distance_y**2)
    angle = math.atan2(distance_y, distance_x)

    print(angle) # in radianti

    pupil_x = eye_x
    pupil_y = eye_y
    
    screen.draw.filled_circle((eye_x, eye_y), eye_r, color=(255, 255, 255))
    screen.draw.filled_circle((pupil_x, pupil_y), pupil_r, color=(0, 0, 0))

def on_mouse_move(pos):
    global mouse_x, mouse_y
    mouse_x, mouse_y = pos