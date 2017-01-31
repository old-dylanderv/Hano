# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
from class_Charac import *
from class_Atk import *
from class_AtkEffect import *
#Hero est la classe générique des héros
#Carastéristiques des héros:
#   Ils sont controlés au clavier
#   Ils peuvent double-sauter
#   Ils ont des spells (définis dans la classe fille)
class Mob(Charac):
    def __init__(self, x, y, width, height, images, weight, baseAcc_x, baseJumpForce, maxSpeed_x, windowWidth, hp, atkList):
        Charac.__init__(self, x, y, width, height, images, weight, baseAcc_x, baseJumpForce, maxSpeed_x, windowWidth, hp, atkList)
        self.states['RmoveLeft'] = 100
        self.states['RmoveRight'] = 100
        self.states['FjumpLeft'] = 100
        self.states['FjumpRight'] = 100
        self.states['FfallLeft'] = 50
        self.states['FfallRight'] = 50
        self.states['RslideLeft'] = 50
        self.states['RslideRight'] = 50
        self.states['FcrouchLeft'] = 50
        self.states['FcrouchRight'] = 50
        self.states['Oaa1Right'] = 75
        self.states['Oaa1Left'] = 75
        self.states['OdmgRight'] = 400
        self.states['OdmgLeft'] = 400
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.autoHit = False
        self.spell1 = False
        self.guard = False
        self.ult = False

    def update(self, fps):
        self.stop()
        Charac.update(self, fps)

    def giveDoubleJump(self):
        self.doubleJump = True
