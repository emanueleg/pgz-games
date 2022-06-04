# ver 02
# posizionamento dell'occhio sul minion

WIDTH = 600
HEIGHT = 700


def draw():
    screen.blit('minion_01', (0, 0))

    eye_x = 288
    eye_y = 182
    eye_r = 77
    pupil_r = 25

    pupil_x = eye_x
    pupil_y = eye_y

    screen.draw.filled_circle((eye_x, eye_y), eye_r, color=(255, 255, 255))
    screen.draw.filled_circle((pupil_x, pupil_y), pupil_r, color=(0, 0, 0))
