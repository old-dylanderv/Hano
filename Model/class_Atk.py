# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
from class_Animated import *
from class_AtkEffect import *

#Atk est la classe générique du manager des attaques
#Carastéristiques du manager:
#   un cooldown s
#   un timer a update dans la boucle de jeu (via le Charac)
#   toutes les informations sur l'attaque à lancer
class Atk():
    def __init__(self, cd, width, height, images, dmg , knockback, weight, speed_x, speed_y, duration):
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
    def get_cd(self):
        return "{0:.2f}".format(self.timer)

    #Facing 1 => droite
    #Facing -1 => gauche
    def launch(self, x, y, facing, combo):
        if(self.timer <= 0):
            self.timer = self.cd
            return self.cast(x, y, facing, combo)
        else:
            return None

    def cast(self, x, y, facing, combo):
        return AtkEffect(x, y, self.width, self.height, self.images, self.dmg*combo , self.knockback, self.weight, self.speed_x*facing, self.speed_y, facing, self.duration)
