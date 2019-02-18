#!/usr/bin/env python3

from random import randint

print("Le programme a choisit un nombre entre 1 et 100, vous devez le trouver")
nb = randint(1,100)
saisie = 0
while saisie != nb:
    saisie = int(input("Entrez un nombre : "))
    if saisie < nb:
        print("Le nombre est supérieur")
        if (saisie+5) >= nb:
            print("Très proche !")
        elif (saisie+10) >= nb:
            print("Proche !")
    elif saisie > nb:
        print("Le nombre est inférieur")
        if (saisie-5) <= nb:
            print("Très proche !")
        elif (saisie-10) <= nb:
            print("Proche !")
    else:
        print("Trouvé !")        
print("Merci d'avoir joué :-)")
