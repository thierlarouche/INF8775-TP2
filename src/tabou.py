import sys
import os
import time
import random
from operator import attrgetter


path = sys.argv[1]
blocAffiche = sys.argv[2]
timer = sys.argv[3]
start = 0
stop = 0


################################################################################

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
    blocSolReserve = []
    blocSolGlouton = []
    listTabou = []
    blocsLeftOut = []
    blocRebuild = []
    listTabouCheck = []
    currentLongeur = 0
    currentProfondeur = 0
    hauteurPile = 0
    iteration = 0

    with open(path, "r") as file:
        for line in file:
            currentLine = line.split()

            # convertir chaque ligne du fichier texte en objet bloc
            currentBloc = bloc(int(currentLine[0]),int(currentLine[1]), int(currentLine[2]), int(currentLine[0]) * int(currentLine[1]))

            blocs.append(currentBloc)
    # debut du timer
    start = time.perf_counter()
    ################################################################################


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

    blocSolReserve.append(blocSolutions[0])
    blocSolGlouton = blocSolutions.copy()

    #debut tabou
    index =0







    while iteration <= 100:
        blocsLeftOut.clear()
        # Trier les blocs qu'on peut utiliser
        for bloc in blocsTries:
            if((not(bloc in blocSolutions)) and (not(bloc in listTabouCheck))):
                blocsLeftOut.append(bloc)
                

        # Trier les blocs leftout selon leur hauteur

        blocsLeftOut = sorted(blocsLeftOut, key=attrgetter('_hauteur'), reverse = True)

        #for bloc in blocsLeftOut :
            #print("bloc pool : " ,bloc._longeur, " ", bloc._profondeur, " ", bloc._hauteur)

        blocToInsert = random.choice(blocsLeftOut)
        blocRebuild.append(blocToInsert)
        # Trouver ou l'inserer
        index=0
        myRange = reversed(range(0, len(blocSolutions)))
        if((blocToInsert._longeur > blocSolutions[0]._longeur ) or (blocToInsert._profondeur > blocSolutions[0]._profondeur)):
            blocRebuild = blocSolutions.copy()
            blocSolutions.clear()
            blocSolutions.append(blocToInsert)
        else :
            for i in myRange:
                if((blocToInsert._longeur < blocSolutions[i]._longeur ) and (blocToInsert._profondeur < blocSolutions[i]._profondeur) and (i != (len(blocSolutions)-1))):
                    blocSolutions.insert(i+1, blocToInsert)
                    break
                elif ((blocToInsert._longeur < blocSolutions[i]._longeur ) and (blocToInsert._profondeur < blocSolutions[i]._profondeur) and (i == (len(blocSolutions)-1))) :
                    blocSolutions.append(blocToInsert)
                    break
                else :
                    blocRebuild.append(blocSolutions[i])
                index = index + 1
            # Vider la solution jusquau nouvel ajout
            length = len(blocSolutions)-index
            while not(len(blocSolutions) <= length):
                blocSolutions.pop()
            blocRebuild.reverse()


        myRange = reversed(range(0, len(blocRebuild)))
        for bloc in blocRebuild:
            if((blocToInsert._longeur > bloc._longeur ) and (blocToInsert._profondeur > bloc._profondeur)):
                blocSolutions.append(bloc)
            else :
                # remplir tabou
                if(not(bloc in listTabouCheck)) :
                    rand = random.randrange(8,12)
                    blocT = blocTabou(rand, bloc)
                    listTabou.append(blocT)
                    listTabouCheck.append(bloc)
        

        # Reduire compteur list Tabou
        for item in listTabou :
            item._random = item._random - 1
            if (item._random == 0) :
                bloc = item._bloc
                listTabou.remove(item)
                for cube in listTabouCheck :
                    if((item._bloc._longeur == cube._longeur) and (item._bloc._profondeur == cube._profondeur)):
                        listTabouCheck.remove(cube)

    #Hauteur Solution
        hauteurSol = 0
        for bloc in blocSolutions :
            hauteurSol = hauteurSol + bloc._hauteur
            #print("Sol :", bloc._longeur, " ", bloc._profondeur, " ", bloc._hauteur)


        hauteurSolReserve = 0
        for bloc in blocSolReserve :
            hauteurSolReserve = hauteurSolReserve + bloc._hauteur
            
        hauteurSolGlouton = 0
        for bloc in blocSolGlouton :
            hauteurSolGlouton = hauteurSolGlouton + bloc._hauteur
            
        
        if(hauteurSol > hauteurSolReserve) :
            blocSolReserve = blocSolutions.copy()
            iteration = 0
        else :
            
            blocSolutions = blocSolReserve.copy()
            iteration = iteration + 1

            if(not(blocToInsert in listTabouCheck)) :
                rand = random.randrange(8,12)
                blocT = blocTabou(rand, blocToInsert)
                listTabou.append(blocT)
                listTabouCheck.append(blocToInsert)


        blocsLeftOut.clear()
        blocRebuild.clear()

    ################################################################################
    #arret du compteur
    stop = time.perf_counter()

    #sortie de la solution
    index=0
    #trouver hauteur solution
    hauteurSol = 0
    for bloc in blocSolutions :
            hauteurSol = hauteurSol + bloc._hauteur

    #imprimer la solution
    if (blocAffiche == "true"):
        for i in myRange:
            print(blocSolutions[i]._hauteur, " ", blocSolutions[i]._longeur, " ", blocSolutions[i]._profondeur)

if(timer == "true"):
    print((stop - start)*1000)