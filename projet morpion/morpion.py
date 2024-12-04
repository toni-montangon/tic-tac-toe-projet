print("Bienvenue sur Tic Tac Toe")
print("-------------------------")

NombrePossible = [1,2,3,4,5,6,7,8,9]
Tableau = [[1,2,3], [4,5,6], [7,8,9]]
Lignes = 3
Colonnes = 3

def printTableau():
    for x in range(Lignes):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(Colonnes):
            print("", Tableau[x][y], end=" |")
    print("\n+---+---+---+")

def modiftableau(num, tour):
    num -= 1
    if(num == 0):
        Tableau[0][0] = tour
    elif(num == 1):
        Tableau[0][1] = tour
    elif(num == 2):
        Tableau[0][2] = tour
    elif(num == 3):
        Tableau[1][0] = tour
    elif(num == 4):
        Tableau[1][1] = tour
    elif(num == 5):
        Tableau[1][2] = tour
    elif(num == 6):
        Tableau[2][0] = tour
    elif(num == 7):
        Tableau[2][1] = tour
    elif(num == 8):
        Tableau[2][2] = tour

def grillegagnante(Tableau):
    # AXE X (Ligne)
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
    
    # AXE Y (Colonne)
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
    
    # AXE (Diagonale)
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

FinBoucle = False
CompteurTour = 0

while not FinBoucle:
    if CompteurTour % 2 == 0:
        printTableau()
        numerochoisi = int(input("\nJoueur 1, c'est à ton tour. Choisis un chiffre entre [1-9]: "))
        if 1 <= numerochoisi <= 9:
            modiftableau(numerochoisi, 'X')
            NombrePossible.remove(numerochoisi)
        else:
            print("Chiffre invalide. Choisis-en un autre.")
        CompteurTour += 1
    else:
        printTableau()
        numerochoisi = int(input("\nJoueur 2, c'est à ton tour. Choisis un chiffre entre [1-9]: "))
        if 1 <= numerochoisi <= 9:
            modiftableau(numerochoisi, 'O')
            NombrePossible.remove(numerochoisi)
        else:
            print("Chiffre invalide. Choisis-en un autre.")
        CompteurTour += 1
    
    Gagnant = grillegagnante(Tableau)
    if Gagnant != "N":
        print("\nMerci d'avoir joué ! :)")
        break