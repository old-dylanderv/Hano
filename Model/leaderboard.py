# -*- coding:Utf-8 -*-

def readFile():
    fichier = open("leaderboard.txt", "r")
    aaa = fichier.read()
    fichier.close()
    aaa = aaa.split(";")
    tabScore = []
    i = 0
    while i < len(aaa) - 1:

        score = aaa[i].split("-")[1]
        j = 0
        while j < len(tabScore) and float(tabScore[j][1]) > float(score):
            j += 1

        newTabScore = []
        k = 0
        while k < j:
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

def addScore(tabScore, score, name):
    j = 0
    i = 9
    if(i > len(tabScore)):
        i = len(tabScore)
    while j < i and float(tabScore[j][1]) > float(score):
        j += 1
    if(j < 10):

        newTabScore = []
        k = 0
        while k < j:
            newTabScore.append(tabScore[k])
            k += 1

        newTabScore.append([name,score])

        while k < i:
            newTabScore.append(tabScore[k])
            k += 1

        del tabScore[:]
        for parcTab in newTabScore:
            tabScore.append(parcTab)

    return tabScore

def writeFile(tabScore):
    fichier = open("leaderboard.txt", "w")
    i = 0
    while i < len(tabScore):
        fichier.write(str(tabScore[i][0])+"-"+str(tabScore[i][1])+";")
        i += 1
