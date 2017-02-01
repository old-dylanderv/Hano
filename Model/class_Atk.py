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
    def __init__(self, nom, cd, width, height, images, dmg , knockback_x, knockback_y, weight, speed_x, speed_y, duration):
        self.nom = nom
        self.cd = cd
        self.timer = 0
        self.dmg = dmg
        self.width = width
        self.height = height
        self.images = images
        self.knockback_x = knockback_x
        self.knockback_y = knockback_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.weight = weight
        self.duration = duration
        self.images = images

    def update(self, fps):
        if(self.timer > 0):
            self.timer = self.timer - (1.0/fps)

    #Sert a lancer le spell a gauche
    def get_width(self):
        return self.width

    def put_on_cd(self):
        self.timer = self.cd

    def put_cd(self, cd):
        self.timer = cd

    #Renvoie un string (pour affichage)
    def get_cd(self):
        return "{0:.2f}".format(self.timer)

    #Facing 1 => droite
    #Facing -1 => gauche
    def launch(self, x, y, facing, combo, bonusSpeed_x = 0, bonusSpeed_y = 0):
        if(self.timer <= 0):
            self.timer = self.cd
            return self.cast(x, y, facing, combo, bonusSpeed_x, bonusSpeed_y)
        else:
            return None

    def cast(self, x, y, facing, combo, bonusSpeed_x, bonusSpeed_y):
        return AtkEffect(self.nom, x, y, self.width, self.height, self.images, self.dmg*combo , self.knockback_x*facing, self.knockback_y, self.weight, self.speed_x*facing+bonusSpeed_x, (self.speed_y+bonusSpeed_y), facing, self.duration)
