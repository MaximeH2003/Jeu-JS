# import random

# def devine_le_nombre():
#     print("Bienvenue dans le jeu Devine le Nombre !")
#     nombre_secret = random.randint(1, 50)
#     essais_restants = 10

#     while essais_restants > 0:
#         print("Il te reste", essais_restants, "essais.")
#         essai = int(input("Devine le nombre entre 1 et 50 : "))

#         if essai < nombre_secret:
#             print("Le nombre secret est plus grand.")
#         elif essai > nombre_secret:
#             print("Le nombre secret est plus petit.")
#         else:
#             print("Félicitations ! Tu as deviné le nombre secret.")
#             break

#         essais_restants -= 1

#     if essais_restants == 0:
#         print("Dommage, tu as épuisé tous tes essais. Le nombre secret était", nombre_secret)

# devine_le_nombre()


import random

def generer_nombre_secret():
    return random.randint(1, 50)

def demander_essai():
    return int(input("Devine le nombre entre 1 et 50 : tu as 10 essai !"))

def comparer_essai(nombre_secret, essai):
    if essai < nombre_secret:
        print("Le nombre secret est plus grand.")
    elif essai > nombre_secret:
        print("Le nombre secret est plus petit.")
    else:
        print("Félicitations ! Tu as deviné le nombre secret.")

def devine_le_nombre():
    print("Bienvenue dans le jeu Devine le Nombre !")
    nombre_secret = generer_nombre_secret()
    essais_restants = 10

    while essais_restants > 0:
        print("Il te reste", essais_restants, "essais.")
        essai = demander_essai()
        comparer_essai(nombre_secret, essai)

        if essai == nombre_secret:
            break

        essais_restants -= 1

    if essais_restants == 0:
        print("Dommage, tu as épuisé tous tes essais. Le nombre secret était", nombre_secret)

devine_le_nombre()