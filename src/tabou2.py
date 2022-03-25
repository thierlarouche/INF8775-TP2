import sys
import os
import time
import random
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

class blocTabou:

    def __init__(self, random, bloc):
        self._random = random
        self._bloc = bloc

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  
    blocs = []
    blocsTries = []
    blocSolutions = []
    listTabou = []
    blocsLeftOut = []
    blocRebuild = []
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
    #debut tabou
    index =0

    # Trier les blocs qu'on peut utiliser
    for bloc in blocsTries:
        if((not(bloc in blocSolutions)) and (not(bloc in listTabou))):
            blocsLeftOut.append(bloc)

    # Trier les blocs leftout selon leur hauteur
    blocsLeftOut = sorted(blocsLeftOut, key=attrgetter('_hauteur'), reverse = True)

    blocToInsert = blocsLeftOut[0]

    # Trouver ou l'inserer
    index=0
    myRange = reversed(range(0, len(blocSolutions)))
    for i in myRange:
        if((blocToInsert._longeur < blocSolutions[i]._longeur ) and (blocToInsert._profondeur < blocSolutions[i]._profondeur)):
            blocSolutions.insert(i+1, blocToInsert)
            break
        else :
            blocRebuild.append(blocSolutions[i])
        index = index + 1

    length = len(blocSolutions)-index
    while not(len(blocSolutions) <= length):
        blocSolutions.pop()
    

    myRange = reversed(range(0, len(blocRebuild)))
    for bloc in blocRebuild:
        if((blocToInsert._longeur > bloc._longeur ) and (blocToInsert._profondeur > bloc._profondeur)):
            blocSolutions.append(bloc)
 ######################################################
# build tabou
 ################################################
    for bloc in blocRebuild :
        rand = random.randrange(7,11)
        blocT = blocTabou(rand, bloc)
        listTabou.append(blocT)

    for bloc in listTabou:
        print("tabou:", bloc._random," ", bloc._bloc._longeur, " ", bloc._bloc._profondeur, " ", bloc._bloc._hauteur )
    #arret du compteur
    stop = time.perf_counter()

    #sortie de la solution
    print("blocs solution glouton : ")
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