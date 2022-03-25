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
    _index = 0
    _Hmax = 0
    _blocPrecedant = 0

    def __init__(self, longeur, profondeur, hauteur, aire, index, Hmax, blocPrecedant):
        self._longeur = longeur
        self._profondeur = profondeur
        self._hauteur = hauteur
        self._aire = aire
        self._index = index
        self._Hmax = Hmax
        self._blocPrecedant = blocPrecedant


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  
    blocs = []
    blocsTriesAire = []
    blocSolutions = []
    currentLongeur = 0
    currentProfondeur = 0
    hauteurPile = 0
    currentBlocIndex = -1
    temporaryHMax = 0
    temporaryIndex = 0
    Hmax = 0
    indexMax = 0

    with open("../b100000_10.txt", "r") as file:
        for line in file:
            currentLine = line.split()

            # convertir chaque ligne du fichier texte en objet bloc
            currentBloc = bloc(int(currentLine[0]),int(currentLine[1]), int(currentLine[2]), int(currentLine[0]) * int(currentLine[1]), 0, 0, 0)
            blocs.append(currentBloc)


    # on trie les blocs selon l'aire
    blocsTriesAire = sorted(blocs, key=attrgetter('_aire'), reverse = True)

    # on attribu un index a chaque bloc du tableau trie selon l'aire
    index = 0
    for bloc in blocsTriesAire:
        bloc._index = index
        index = index + 1



    # iteration a travers la liste de bloc trie
    for bloc in blocsTriesAire :
        temporaryHMax = 0
        temporaryIndex = 0
        if (bloc._index == 0):
            bloc._Hmax = bloc._hauteur
            bloc._blocPrecedant = -1

        else :
            myRange = reversed(range(0, bloc._index)) #####
            for blocUnder in myRange :
                if((bloc._longeur < blocsTriesAire[blocUnder]._longeur) and (bloc._profondeur < blocsTriesAire[blocUnder]._longeur)) :
                    # on sauvegarde le bloc ayant le plus grand Hmax, optimisation au lieu de garder une liste des solutions possible
                    if(temporaryHMax < blocsTriesAire[blocUnder]._Hmax) :
                        temporaryHMax = blocsTriesAire[blocUnder]._Hmax
                        temporaryIndex = blocsTriesAire[blocUnder]._index
        bloc._blocPrecedant = temporaryIndex
        bloc._Hmax = bloc._hauteur + temporaryHMax      

    # trouver le bloc ayant le plus grand Hmax
    for bloc in blocsTriesAire :
        if(bloc._Hmax > Hmax) :
            Hmax = bloc._Hmax
            indexMax = bloc._index

    # trouver la solution
    blocSolutions.append(blocsTriesAire[indexMax])
    myRange = reversed(range(0, indexMax+1))
    currentIndex = blocsTriesAire[indexMax]._blocPrecedant
    for bloc in myRange :
        if (currentIndex == blocsTriesAire[bloc]._index) and (blocsTriesAire[bloc]._index >= 0) :
            currentIndex = blocsTriesAire[bloc]._blocPrecedant
            blocSolutions.append(blocsTriesAire[bloc])

    #arret du compteur
    stop = time.perf_counter()

    #sortie de la solution
    print("blocs solution : ")
    index=0
    for bloc in blocSolutions:
        index = index+1
        print(index, " : " ,bloc._longeur, " ", bloc._profondeur, " ", bloc._hauteur)
    print("Hauteur : ")
    print(Hmax)

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