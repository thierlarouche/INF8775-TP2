import sys
import os
import time
from operator import attrgetter


path = sys.argv[1]
blocAffiche = sys.argv[2]
timer = sys.argv[3]
start = 0
stop = 0


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
    currentLongeur = 0
    currentProfondeur = 0
    hauteurPile = 0

    #Convertir chaque ligne du fichier texte en objet bloc
    with open(path, "r") as file:
        for line in file:
            currentLine = line.split()

            # conversion en objet
            currentBloc = bloc(int(currentLine[0]),int(currentLine[1]), int(currentLine[2]), int(currentLine[0]) * int(currentLine[1]))

            blocs.append(currentBloc)


    if(timer == "true"):
        start = time.perf_counter()
    ################################################################################

    #On trie les blocs selon l'aire
    blocsTries = sorted(blocs, key=attrgetter('_aire'), reverse = True)

    # traitement du premier bloc
    blocSolutions.append(blocsTries[0])
    currentLongeur = blocSolutions[0]._longeur
    currentProfondeur= blocSolutions[0]._profondeur
    hauteurPile = blocSolutions[0]._hauteur

    #Etape 3: Ajout des blocs dans l'ensemble solution
    for bloc in blocsTries:
        #on ajoute les blocs strictement plus petit dans l'ensemble solution
        if((bloc._longeur < currentLongeur) and (bloc._profondeur < currentProfondeur)) :
            currentLongeur = bloc._longeur
            currentProfondeur = bloc._profondeur
            blocSolutions.append(bloc)
            hauteurPile += bloc._hauteur

    #arret du compteur
    stop = time.perf_counter()



################################################################################

    #sortie de la solution

    index=0

    myRange = (range(0, len(blocSolutions)))
    if (blocAffiche == "true"):
        for i in myRange :
            index = index+1
            print(blocSolutions[i]._hauteur, " ", blocSolutions[i]._longeur, " ", blocSolutions[i]._profondeur)
    #print(hauteurPile)
if(timer == "true"):
    print((stop - start)*1000)