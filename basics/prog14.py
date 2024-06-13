import random

n_tentativi = 3
dado = random.randint(1, 6)

for i in range(n_tentativi):
    risposta = int(input("Indovina... "))
    if risposta == dado:
        print(":-)")
        break
    else:
        if i < 2:
            print("Ritenta")
        else:
            print(":-(")