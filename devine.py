__author__ = 'Jacques Supcik'

import random

print("Je vais penser à un nombre entre 0 et 100.")
print("Essaye de le deviner!")

secret = random.randint(0, 101)
coups = 0

while True:
    essai = int(input("Que proposes-tu ? "))
    coups += 1

    if essai < secret:
        print("Trop petit")
    elif essai > secret:
        print("Trop grand")
    else:
        print("Bravo! tu as gagné en {0} coups".format(coups))
        break