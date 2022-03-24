import sys
import os
import time
from operator import attrgetter


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
    currentLongeur = 0
    currentProfondeur = 0
    hauteurPile = 0

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

    for bloc in blocsTries:

        #on ajoute les blocs strictement plus petit dans l'ensemble solution
        if((bloc._longeur < currentLongeur) and (bloc._profondeur < currentProfondeur)) :
            currentLongeur = bloc._longeur
            currentProfondeur = bloc._profondeur
            blocSolutions.append(bloc)
            hauteurPile += bloc._hauteur

    #arret du compteur
    stop = time.perf_counter()

    #sortie de la solution
    print("blocs solution : ")
    index=0
    for bloc in blocSolutions:
        index = index+1
        print(index, " : " ,bloc._longeur, " ", bloc._profondeur, " ", bloc._hauteur)
    print("hauteur Pile : ")
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