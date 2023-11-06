from random import randint

def play_game(maxPoint):
    Pointsjoueur = 0
    Pointsordinateur = 0
    jeu = ["pierre", "papier", "ciseaux"]
    continuer = True

    while continuer:
        ordinateur = jeu[randint(0, 2)]
        joueur = input("pierre, papier, ciseaux? ou tapez 'Fin' pour arrêter le jeu! Ecris 'stats' pour voir les points\n")
        
        if joueur == 'Fin':
            continuer = False
        
        if Pointsordinateur == maxPoint or Pointsjoueur == maxPoint:
            continuer = False
        
        elif joueur == "stats":
            display_scores(Pointsjoueur, Pointsordinateur)
        
        elif joueur in ["pierre", "papier", "ciseaux"]:
            result = determine_winner(joueur, ordinateur)
            update_scores(result, Pointsjoueur, Pointsordinateur)
        
        else:
            print("Votre choix n'est pas correct, vérifiez l'orthographe !")

def display_scores(Pointsjoueur, Pointsordinateur):
    print("Points du joueur :", Pointsjoueur)
    print("Points de l'ordinateur :", Pointsordinateur)

def determine_winner(joueur, ordinateur):
    if joueur == "pierre":
        if ordinateur == "papier":
            return "ordinateur"
        elif ordinateur == "ciseaux":
            return "joueur"
    
    elif joueur == "papier":
        if ordinateur == "ciseaux":
            return "ordinateur"
        elif ordinateur == "pierre":
            return "joueur"
    
    elif joueur == "ciseaux":
        if ordinateur == "pierre":
            return "ordinateur"
        elif ordinateur == "papier":
            return "joueur"

def update_scores(result, Pointsjoueur, Pointsordinateur):
    if result == "joueur":
        print("Gagné!")
        Pointsjoueur += 1
    elif result == "ordinateur":
        print("Perdu!")
        Pointsordinateur += 1
    else:
        print("Egalité!")
    
    return Pointsjoueur, Pointsordinateur

if __name__ == '__main__':
    maxPoint = int(input("Définissez un maximum de points à atteindre :\n"))
    play_game(maxPoint)
    
    

# from random import randint
# Pointsjoueur = 0
# Pointsordinateur = 0
# continuer = True
# jeu  = ["pierre", "papier", "ciseaux"]
# maxPoint = 0

# maxPoint = int(input("Déinissez un max de point à atteindre :\n"))
# while(continuer == True):
#     ordinateur = jeu[randint(0,2)]
#     joueur = input("pierre, papier, ciseaux? ou tapez 'Fin' pour arrêter le jeu! Ecris 'stats' pour voir les point\n")
#     if(joueur == 'Fin'):
#         continuer = False
#     if(Pointsordinateur == maxPoint or Pointsjoueur == maxPoint):
#         continuer = False
#     elif(joueur=="stats"):
#         print("point du joueur :", Pointsjoueur)
#         print("point de l'ordinateur :", Pointsordinateur)
#     elif(joueur == ordinateur):
#         print("Egalité!")
#     elif(joueur == "pierre"):
#         if(ordinateur == "papier"):
#             print("Perdu!", ordinateur, "recouvre", joueur)
#             Pointsordinateur = Pointsordinateur + 1 
#         else:
#             print("Gagné!", joueur, "écrase", ordinateur)
#             Pointsjoueur = Pointsjoueur + 1
#     elif(joueur == "papier"):
#         if(ordinateur == "ciseaux"):
#             print("Perdu!", ordinateur, "découpe", joueur)
#             Pointsordinateur = Pointsordinateur + 1
#         else:
#             print("Gagné!", joueur, "recouvre", ordinateur)
#             Pointsjoueur = Pointsjoueur + 1
#     elif(joueur == "ciseaux"):
#         if(ordinateur == "Rock"):
#             print("Perdu...", ordinateur, "écrase", joueur)
#             Pointsordinateur = Pointsordinateur + 1
#         else:
#             print("Gagné!", joueur, "découpe", ordinateur)
#             Pointsjoueur = Pointsjoueur + 1
#     else:
#         print("Votre choix n'est pas correct, vérifiez l'orthographe!")
    