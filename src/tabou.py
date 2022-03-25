import sys
import os
import time
from operator import attrgetter
import numpy as np

# path = sys.argv[1]
# bloc = sys.argv[2]
# timer = sys.argv[3]
# start = 0
# stop = 0

# if(timer == "true"):
    
start = time.perf_counter()
################################################################################

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class bloc:
    _longeur = 0
    _profondeur = 0
    _hauteur = 0
    _aire = 0

    def __init__(self, longeur, profondeur, hauteur,aire):
        self._longeur = longeur
        self._profondeur = profondeur
        self._hauteur = hauteur
        self._aire = aire
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  
    blocs = []
    blocsTries = []
    blocSolutions = []
    solutionGlouton = []
    solutionTemporaire = []
    blocTabou = []
    currentLongeur = 0
    currentProfondeur = 0
    hauteurPile = 0
    positionBlocAjoute = 0
    hauteurMax = 0
    tourDeBoucle = 0
    hauteurTemporaire = 0
    
    with open("../b100_1.txt", "r") as file:
        for line in file:
            currentLine = line.split()

            # convertir chaque ligne du fichier texte en objet bloc
            currentBloc = bloc(int(currentLine[0]),int(currentLine[1]), int(currentLine[2]), int(currentLine[0]) * int(currentLine[1]))

            blocs.append(currentBloc)


    # on trie les blocs selon l'aire
    blocsTries = sorted(blocs, key=attrgetter('_aire'), reverse = True)

    # traitement du premier bloc
    blocSolutions.append(blocsTries[0])
    currentLongeur = blocSolutions[0]._longeur
    currentProfondeur= blocSolutions[0]._profondeur
    hauteurPile = blocSolutions[0]._hauteur
    print(blocs[0]._hauteur)
    for bloc in blocsTries:

        #on ajoute les blocs strictement plus petit dans l'ensemble solution
        if((bloc._longeur < currentLongeur) and (bloc._profondeur < currentProfondeur)) :
            currentLongeur = bloc._longeur
            currentProfondeur = bloc._profondeur
            blocSolutions.append(bloc)
            hauteurPile += bloc._hauteur
    hauteurMax = hauteurPile
    solutionGlouton = blocSolutions.copy()
    solutionTemporaire = blocSolutions.copy()

    # regarder tous les bloc qui sont ni dans la solution ni dans la liste tabou
    for bloc in blocsTries:
        if((not(bloc in blocSolutions)) and (not(bloc in blocTabou))):

            # trouver la position ou on peut inserer notre bloc voisin
            myRange = reversed(range(0, len(blocSolutions)))
            index = len(blocSolutions)
            positionTrouve = False
            # On itere a travers les blocs de notre solution
            for blocVoisin in myRange:
                #print("blocvoisin ", blocVoisin)
                
                # on regarde la position la plus haute sur laquelle on peu poser le bloc voisin
                if((bloc._longeur < blocSolutions[blocVoisin]._longeur) and (bloc._profondeur < blocSolutions[blocVoisin]._profondeur)):
                    
                    # ajout du bloc voisin selectionne dans la solution
                    blocSolutions.insert(blocVoisin, bloc)
                    positionTrouve = True
                    #parcourir les blocs dans la solution a partir du bloc ajoute
                    positionBlocAjoute = blocVoisin
                    myRange = reversed(range(0, positionBlocAjoute))
                    longeurReference = blocSolutions[blocVoisin]._longeur
                    profondeurReference = blocSolutions[blocVoisin]._profondeur
                    # parcourir la liste pour retirer les blocs trop grands suite a l'insertion de notre nouveau bloc
                    print(positionBlocAjoute)

                    for blocSol in myRange:
                        print("hauteur max", hauteurMax, "hauteur temporaire ", hauteurTemporaire) 
                        #verifier si le blocVoisin est plus petit que le bloc
                        if((longeurReference <= blocSolutions[blocSol]._longeur) and (profondeurReference <= blocSolutions[blocSol]._profondeur)):
                            # ajout a la liste tabou
                            blocTabou.append(blocSolutions[blocSol])
                            # 
                            del blocSolutions[blocSol]
                            
                            # trouver la hauteur de notre nouvelle tourVoisin
                            for bloc in blocSolutions :
                                hauteurTemporaire += bloc._hauteur
                            #verifier si elle est plus grande que notre solution precedante
                if(hauteurMax < hauteurTemporaire):
                    solutionTemporaire = blocSolutions.copy()
                    hauteurMax = hauteurTemporaire
                    print("test")
                else :
                    blocSolutions = solutionTemporaire.copy()
                    tourDeBoucle = tourDeBoucle + 1

                if (positionTrouve):
                    break
        if(tourDeBoucle >= 100):
            break



            index=index-1

            

    #arret du compteur
    stop = time.perf_counter()

    #sortie de la solution
    print("blocs solution : ")
    index=0
    for bloc in solutionTemporaire:
        index = index+1
        print(index, " : " , bloc._longeur, " ", bloc._profondeur, " ", bloc._hauteur)
    print("hauteur Pile : ")
    print(hauteurPile)
    print("hauteur trouvee : ")
    print(hauteurPile)
        
################################################################################
""" mastring = "sol_"
string = mastring + path
f = open(string, "a")
for point in pointcritsolution:
    string = " "
    Sol = " "
    f.write(str(point._x, " ", point._y))
    f.write("_")
f.close() """

################################################################################
# if(timer == "true"):

print((stop - start)*1000)