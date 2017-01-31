# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
from class_Animated import *

#Atk est la classe générique des attaques
#Carastéristiques des attaques:
#   des dégâts (dmg)
#   un cooldown (cd)
#   une force de répulsion (knockback)
class Atk(Animated):
    def __init__(self, x, y, width, height, images, dmg, cd, knockback):
        Animated.__init__(self, x, y, width, height, images)
        self.dmg = dmg
        self.cd = cd
        self.timer = 0
        self.knockback = knockback

    def update(self, fps):
        if(self.timer > 0):
            self.timer = self.timer - (1.0/fps)

    #Renvoie un string (pour affichage)
    def getCd(self):
        return "{0:.2f}".format(self.timer)

    def launch(self):
        if(self.timer <= 0):
            self.timer = cd
            cast()

    def cast(self):
