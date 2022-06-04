# ver 01
# disegno di un semplice occhio statico

WIDTH = 600
HEIGHT = 700


def draw():
    screen.fill((0, 0, 0))

    eye_x = 300
    eye_y = 200
    eye_r = 80
    pupil_r = 25

    pupil_x = eye_x
    pupil_y = eye_y

    screen.draw.filled_circle((eye_x, eye_y), eye_r, color=(255, 255, 255))
    screen.draw.filled_circle((pupil_x, pupil_y), pupil_r, color=(0, 0, 0))
