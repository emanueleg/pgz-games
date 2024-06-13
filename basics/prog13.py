import random

n = int(input("quanti lanci? "))

for i in range(n):
    dado = random.randint(1, 6)
    print(dado)