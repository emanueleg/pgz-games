# ver 04
# creo un mazzo globale e se clicco sul reto di una carta stampo cosa c'è dietro

import random

WIDTH = 1200
HEIGHT = 650

n_cards = 18
cols = 6
deck = []

def draw():
    screen.clear()
    screen.blit('grass', (0, 0))
    
    deck_vals = 2 * [x for x in range(1, 1 + n_cards//2)]
    random.shuffle(deck_vals)

    for i in range(0, n_cards):
        a = Actor('back')
        c = i % cols
        r = i // cols
        a.pos = 100 + 200*c, 100 + 200*r
        a.val = deck_vals[i]
        deck.append(a)
        a.draw()

def on_mouse_down(pos):
    global deck, n_cards
    for i in range(0, n_cards):
        if deck[i].collidepoint(pos):
            print(deck[i].val)