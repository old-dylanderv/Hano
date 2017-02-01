# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
from class_Animated import *

#Charac est la classe générique des mobs, des boss et du héro
#Charac possede:
#   un poids (weight) qui détermine la vitesse de leur chute
#   une vitesse (speed_x et speed_y)
#   une force de saut (baseJumpForce)
#   une poussée en x (baseAcc_x)
#   une accélération en x (currAcc_x)
#   une vitesse maximale en x
#   une orientation (1 = droite, -1 = gauche)
#   un coefficient de frottement lié au milieu
#   des PV
class Charac(Animated):
    def __init__(self, x, y, width, height, images, weight, baseAcc_x, baseJumpForce, maxSpeed_x, windowWidth, hp, atkList):
        Animated.__init__(self, x, y, width, height, images)
        self.weight = weight
        self.facing = 1
        self.onGround = False
        self.speed_x = 0
        self.speed_y = 0
        self.baseAcc_x = baseAcc_x
        self.currAcc_x = 0
        self.baseJumpForce = -1*baseJumpForce
        self.maxSpeed_x = maxSpeed_x
        self.friction = 1
        self.windowWidth = windowWidth
        self.hpMax = hp
        self.hp = hp
        self.atkList = atkList
        self.atkEffectList = []

    def update(self, fps):
        #Bloc de gestion de la vitesse en x
        self.speed_x += self.currAcc_x
        if(self.speed_x > self.maxSpeed_x):
            self.speed_x = self.maxSpeed_x
        elif(self.speed_x < -self.maxSpeed_x):
            self.speed_x = -self.maxSpeed_x
        self.x += self.speed_x
        if(self.x < 0):
            self.x = 0
            self.speed_x = 0
        elif(self.x + self.rect.width > self.windowWidth):
            self.x = self.windowWidth - self.rect.width
            self.speed_x = 0

        #Bloc de gestion de la vitesse en y
        if(self.onGround == True):
            self.speed_y = 0
        else:
            self.speed_y += self.weight
            self.y += self.speed_y
            self.friction = 0.4

        #Gestion des spells
        i = 0
        while(i < len(self.atkEffectList)):
            self.atkEffectList[i].update(fps)
            if(self.atkEffectList[i].isLive() == False):
                self.deleteAtkEffect(i)
            else:
                i += 1

        nbAtk = len(self.atkList)
        for i in range (0, nbAtk):
            self.atkList[i].update(fps)

        #Animation du Charac
        Animated.update(self)

    #On sépare cette fonction de l'update pour pouvoir la personnaliser dans Hero
    def deleteAtkEffect(self, i):
        self.atkEffectList.pop(i)

    def get_AtkEffectList(self):
        return self.atkEffectList

    def get_cd(self, indexAtk):
        return self.atkList[indexAtk].get_cd()

    def jump(self):
        self.speed_y = self.baseJumpForce
        self.onGround = False

    def moveLeft(self):
        self.facing = -1
        self.currAcc_x = -self.baseAcc_x*self.friction

    def moveRight(self):
        self.facing = 1
        self.currAcc_x = self.baseAcc_x*self.friction

    def stop(self):
        if(self.speed_x > 1):
            self.currAcc_x = -self.baseAcc_x*self.friction
        elif(self.speed_x < -1):
            self.currAcc_x = self.baseAcc_x*self.friction
        else:
            self.speed_x = 0
            self.currAcc_x = 0

    def setOnAir(self):
        self.onGround = False

    def isOnGround(self):
        return self.onGround

    def get_hp(self):
        return self.hp

    def set_hp(self, dmg):
        self.hp -= dmg

    def get_hpMax(self):
        return self.hpMax

    def get_onGround(self):
        return self.onGround

    def testPlatform(self, platform):
        if(self.x + self.rect.width -15 > platform.get_x1() and self.x+15 < platform.get_x2()):
            if(self.y + self.rect.height <= platform.get_y() and self.y + self.rect.height + self.speed_y + self.weight >= platform.get_y()):
                self.onGround = True
                self.speed_y = 0
                self.friction = platform.get_friction()
                self.y = platform.get_y() - self.rect.height

    def testAtkEffect(self, atkEffect):
        if(self.x + self.rect.width -15 > atkEffect.get_x1() and self.x+15 < atkEffect.get_x2()):
            if(self.y + self.rect.height >= atkEffect.get_y1() and self.y <= atkEffect.get_y2()):
                self.speed_x += atkEffect.get_knockBack_x()
                self.speed_y += atkEffect.get_knockBack_y()
                if(self.onGround == True and self.speed_y > 0):
                    self.speed_y = atkEffect.get_knockBack_y()*-0.5
                self.onGround = False
                self.set_hp(atkEffect.get_dmg())
                atkEffect.delete()
                if(self.facing == 1):
                    Animated.changeState(self, "OdmgRight")
                else:
                    Animated.changeState(self, "OdmgLeft")
