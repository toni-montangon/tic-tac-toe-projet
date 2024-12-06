print("Bienvenue sur Tic Tac Toe")
print("-------------------------")

NombrePossible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Tableau = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Lignes = 3
Colonnes = 3

def printTableau():
    for x in range(Lignes):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(Colonnes):
            print("", Tableau[x][y], end=" |")
    print("\n+---+---+")

def modiftableau(num, tour):
    num -= 1
    if num == 0:
        Tableau[0][0] = tour
    elif num == 1:
        Tableau[0][1] = tour
    elif num == 2:
        Tableau[0][2] = tour
    elif num == 3:
        Tableau[1][0] = tour
    elif num == 4:
        Tableau[1][1] = tour
    elif num == 5:
        Tableau[1][2] = tour
    elif num == 6:
        Tableau[2][0] = tour
    elif num == 7:
        Tableau[2][1] = tour
    elif num == 8:
        Tableau[2][2] = tour

def grillegagnante(Tableau):
    # AXE X (Ligne horizontal)
    if(Tableau[0][0] == 'X' and Tableau[0][1] == 'X' and Tableau[0][2] == 'X'):
        print("X a gagné!")
        return "X"
    elif(Tableau[0][0] == 'O' and Tableau[0][1] == 'O' and Tableau[0][2] == 'O'):
        print("O a gagné!")
        return "O"
    elif(Tableau[1][0] == 'X' and Tableau[1][1] == 'X' and Tableau[1][2] == 'X'):
        print("X a gagné!")
        return "X"
    elif(Tableau[1][0] == 'O' and Tableau[1][1] == 'O' and Tableau[1][2] == 'O'):
        print("O a gagné!")
        return "O"
    elif(Tableau[2][0] == 'X' and Tableau[2][1] == 'X' and Tableau[2][2] == 'X'):
        print("X a gagné!")
        return "X"
    elif(Tableau[2][0] == 'O' and Tableau[2][1] == 'O' and Tableau[2][2] == 'O'):
        print("O a gagné!")
        return "O"
    
    # AXE Y (Ligne vertical)
    if(Tableau[0][0] == 'X' and Tableau[1][0] == 'X' and Tableau[2][0] == 'X'):
        print("X a gagné!")
        return "X"
    elif(Tableau[0][0] == 'O' and Tableau[1][0] == 'O' and Tableau[2][0] == 'O'):
        print("O a gagné!")
        return "O"
    elif(Tableau[0][1] == 'X' and Tableau[1][1] == 'X' and Tableau[2][1] == 'X'):
        print("X a gagné!")
        return "X"
    elif(Tableau[0][1] == 'O' and Tableau[1][1] == 'O' and Tableau[2][1] == 'O'):
        print("O a gagné!")
        return "O"
    elif(Tableau[0][2] == 'X' and Tableau[1][2] == 'X' and Tableau[2][2] == 'X'):
        print("X a gagné!")
        return "X"
    elif(Tableau[0][2] == 'O' and Tableau[1][2] == 'O' and Tableau[2][2] == 'O'):
        print("O a gagné!")
        return "O"
    
    # AXE (Ligne diagonale)
    if(Tableau[0][0] == 'X' and Tableau[1][1] == 'X' and Tableau[2][2] == 'X'):
        print("X a gagné!")
        return "X"
    elif(Tableau[0][0] == 'O' and Tableau[1][1] == 'O' and Tableau[2][2] == 'O'):
        print("O a gagné!")
        return "O"
    elif(Tableau[0][2] == 'X' and Tableau[1][1] == 'X' and Tableau[2][0] == 'X'):
        print("X a gagné!")
        return "X"
    elif(Tableau[0][2] == 'O' and Tableau[1][1] == 'O' and Tableau[2][0] == 'O'):
        print("O a gagné!")
        return "O"
    
    return "N"

def matchNul():
    # Vérifie si toutes les cases sont remplies
    for i in range(Lignes):
        for j in range(Colonnes):
            if Tableau[i][j] not in ['X', 'O']:
                return False
    return True

FinBoucle = False
CompteurTour = 0

while not FinBoucle:
    printTableau()
    
    if CompteurTour % 2 == 0:
        joueur = 1
        symbole = 'X'
    else:
        joueur = 2
        symbole = 'O'
        
    numerochoisi = int(input(f"\nJoueur {joueur}, c'est à ton tour. Choisis un chiffre entre [1-9]: "))

    # Vérification si le chiffre est bien choisi entre 1 et 9
    if numerochoisi not in NombrePossible:
        print("Chiffre invalide ou déjà utilisé. Choisis-en un autre.")
        continue
    
    # Vérification case déjà occupée
    num_ligne, num_colonne = divmod(numerochoisi - 1, 3)
    if Tableau[num_ligne][num_colonne] in ['X', 'O']:
        print("Cette case est déjà occupée. Choisis une autre case.")
        continue

    modiftableau(numerochoisi, symbole)
    NombrePossible.remove(numerochoisi)
    
    Gagnant = grillegagnante(Tableau)
    
    if Gagnant != "N":
        printTableau()
        print(f"\nJoueur {1 if Gagnant == 'X' else 2} a gagné ! :)")
        break
    elif matchNul():
        printTableau()
        print("\nMatch nul! :)")
        break

    CompteurTour += 1

print("\nMerci d'avoir joué ! :)")

