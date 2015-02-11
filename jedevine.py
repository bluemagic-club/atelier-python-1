__author__ = 'Jacques Supcik'


min = 0
max = 1000
coups = 1

print ("Pense à un nombre entre {0} et {1} et je vais essayer de le deviner".format(min, max))
input ("Presse la touche ENTER quand tu es prêt")


while True:
    x = (min + max) // 2

    print ("Je propose {0}".format(x))
    reponse = input ("Ecris '-' si c'est trop grand et '+', c'est trop petit, et 'x' si j'ai trouvé ? ")

    if reponse == '+':
        coups += 1
        min = x
    elif reponse == '-':
        max = x
        coups += 1
    elif reponse == 'x':
        print ("-" * 60)
        print ("Merci. J'ai trouvé en {0} coups".format(coups))
        print ("C'était un plaisir de jouer avec toi")
        print ("-" * 60)
        break
    else:
        print ("je n'ai pas compris :-(")
