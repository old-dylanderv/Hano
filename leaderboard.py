# -*- coding:Utf-8 -*-

fichier = open("leaderboard.txt", "r")
print(fichier.read())
fichier.close()
fichier = open("leaderboard.txt", "a")
fichier.write("Mdr j'ai pété")
fichier.close()
fichier = open("leaderboard.txt", "r")
print(fichier.read())
