# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
from class_Animated import *

#Atk Effect est le spell en lui meme
#Carastéristiques des atk effect:
#   un set d'images (pas d'état)
#   des dégâts (dmg)
#   une force de répulsion px/fps(knockback)
#   une durée ms(duration) => l'attaque disparait au contact de toute façon
#   un poids acc_y(weight)
#   une vitesse initiale px/fps (speed_x et speed_y)
class AtkEffect(Animated):
    def __init__(self, x, y, width, height, images, dmg , knockback, weight, speed_x, speed_y, facing, duration):
        Animated.__init__(self, x, y, width, height, images)
        self.x1 = x
        self.x2 = x + width
        self.y1 = y
        self.y2 = y + height
        self.states["idleRight"] = 75
        self.states["idleLeft"] = 75
        self.dmg = dmg
        self.knockback = knockback
        self.weight = weight
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.duration = duration
        self.images = images
        if(facing == 1):
            Animated.changeState(self, "idleRight")
        else:
            Animated.changeState(self, "idleLeft")

    def get_x1(self):
        return self.x1

    def get_x2(self):
        return self.x2

    def get_y1(self):
        return self.y1

    def get_y2(self):
        return self.y2

    def get_knockBack(self):
        return self.knockback

    def get_dmg(self):
        return self.dmg

    def get_duration(self):
        return self.duration

    def isLive(self):
        return self.duration > 0

    def delete(self):
        self.duration = 0

    def update(self, fps):
        if(self.duration > 0):
            self.duration = self.duration - (1000/fps)
            self.speed_y += self.weight
            self.x += self.speed_x
            self.y += self.speed_y
            Animated.update(self)
