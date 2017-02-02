# -*- coding:Utf-8 -*-

def readFile():
    fichier = open("leaderboard.txt", "r")
    aaa = fichier.read()
    fichier.close()
    print(aaa)
    aaa = aaa.split(";")
    print aaa
    tabScore = []
    i = 0
    while i < len(aaa) - 1:

        score = aaa[i].split("-")[1]
        j = 0
        while j < len(tabScore) and int(tabScore[j][1]) > int(score):
            j += 1

        newTabScore = []
        k = 0
        while k < j:
            print(k)
            newTabScore.append(tabScore[k])
            k += 1

        newTabScore.append([aaa[i].split("-")[0],score])


        while k < len(tabScore):
            newTabScore.append(tabScore[k])
            k += 1

        del tabScore[:]
        for parcTab in newTabScore:
            tabScore.append(parcTab)

        i += 1
    return tabScore


def writeFile(tabScore):
    fichier = open("leaderboard.txt", "w")
    i = 0
    while i < len(tabScore):
        fichier.write(tabScore[i][0]+"-"+tabScore[i][1]+";")
        i += 1
