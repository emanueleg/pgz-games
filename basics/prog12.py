import random

dado = random.randint(1, 6)

risposta = int(input("Prova a indovinare... "))

if dado == risposta:
    print("Hai indovinato!")
else:
    print("Sbagliato, è uscito ", dado)