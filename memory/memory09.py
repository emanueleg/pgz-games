# ver 09
# gestiamo le coppie, ricopriamo ogni 2 carte scoperte

import random

WIDTH = 1200
HEIGHT = 650

n_cards = 18
cols = 6
deck = []
shown = []

def reset():
    global deck, n_cards
    deck_vals = 2 * [x for x in range(1, 1 + n_cards//2)]
    random.shuffle(deck_vals)

    for i in range(0, n_cards):
        a = Actor('back')
        c = i % cols
        r = i // cols
        a.pos = 100 + 200*c, 100 + 200*r
        a.val = deck_vals[i]
        a.status = "nascosto"  # nascosto / visibile / preso
        deck.append(a)

def draw():
    screen.clear()
    screen.blit('grass', (0, 0))

    for i in range(0, n_cards):
        if deck[i].status == "nascosto":
            deck[i].image = "back"
            deck[i].draw()
        elif deck[i].status == "visibile":
            deck[i].image = str(deck[i].val)
            deck[i].draw()

def hide_all():
    global deck
    for i in range(0, n_cards):
        if deck[i].status == "visibile":
            deck[i].status = "nascosto"

def clicked_card(i):
    global deck, shown

    if deck[i].status == "preso":
        return

    if len(shown) == 2:
        hide_all()
        shown = []

    if deck[i].status == "nascosto":
        deck[i].status = "visibile"
        shown.append(i)

def on_mouse_down(pos):
    global deck, n_cards
    for i in range(0, n_cards):
        if deck[i].collidepoint(pos):
            clicked_card(i)

reset()