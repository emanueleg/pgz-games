# ver 03
# catturiamo la posizione del mouse (ma non ci facciamo ancora nulla)

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

    pupil_x = eye_x
    pupil_y = eye_y

    screen.draw.filled_circle((eye_x, eye_y), eye_r, color=(255, 255, 255))
    screen.draw.filled_circle((pupil_x, pupil_y), pupil_r, color=(0, 0, 0))

def on_mouse_move(pos):
    global mouse_x, mouse_y
    mouse_x, mouse_y = pos