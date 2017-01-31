# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
from class_Animated import *

#Atk est la classe générique du manager des attaques
#Carastéristiques du manager:
#   un cooldown s
#   un timer a update dans la boucle de jeu (via le Charac)
#   toutes les informations sur l'attaque à lancer
class Atk():
    def __init__(self, cd, width, height, images, dmg , knockback, weight = 0, speed_x = 0, speed_y = 0, duration):
        self.cd = cd
        self.timer = 0
        self.dmg = dmg
        self.width = width
        self.height = height
        self.images = images
        self.knockback = knockback
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.weight = weight
        self.duration = duration
        self.images = images

    def update(self, fps):
        if(self.timer > 0):
            self.timer = self.timer - (1.0/fps)

    #Renvoie un string (pour affichage)
    def getCd(self):
        return "{0:.2f}".format(self.timer)

    def launch(self, x, y, combo = 1):
        if(self.timer <= 0):
            self.timer = cd
            return cast(x, y, combo)
        else:
            return None
            
    def cast(self, x, y, combo):
        return AtkEffect(x, y, self.width, self.height, self.images, self.dmg*combo , self.knockback, self.weight, self.speed_x, self.speed_y, self.duration)
