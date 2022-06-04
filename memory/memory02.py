# ver 02
# gioco base, dispongo il fronte delle carte

WIDTH = 1200
HEIGHT = 650

n_cards = 18
cols = 6


def draw():
    screen.clear()
    screen.blit('grass', (0, 0))
    
    deck_vals = 2 * [x for x in range(1, 1 + n_cards//2)]

    for i in range(0, n_cards):
        a = Actor(str(deck_vals[i]))
        c = i % cols
        r = i // cols
        a.pos = 100 + 200*c, 100 + 200*r
        a.draw()