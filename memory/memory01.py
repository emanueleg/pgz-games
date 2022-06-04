# ver 01
# gioco base, dispongo il mazzo

WIDTH = 1200
HEIGHT = 650

n_cards = 18
cols = 6


def draw():
    screen.clear()
    screen.blit('grass', (0, 0))
    
    for i in range(0, n_cards):
        a = Actor('back')
        c = i % cols
        r = i // cols
        a.pos = 100 + 200*c, 100 + 200*r
        a.draw()
