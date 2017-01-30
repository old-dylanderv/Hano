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
#   une orientation (0 = droite, 1 = gauche)
#   un coefficient de frottement lié au milieu
class Charac(Animated):
    def __init__(self, x, y, width, height, images, weight, baseAcc_x, baseJumpForce, maxSpeed_x, windowWidth):
        Animated.__init__(self, x, y, width, height, images)
        self.weight = weight
        self.facing = 0
        self.onGround = False
        self.speed_x = 0
        self.speed_y = 0
        self.baseAcc_x = baseAcc_x
        self.currAcc_x = 0
        self.baseJumpForce = -1*baseJumpForce
        self.maxSpeed_x = maxSpeed_x
        self.friction = 1
        self.windowWidth = windowWidth

    def update(self):
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
        Animated.update(self)

    def jump(self):
        self.speed_y = self.baseJumpForce
        self.onGround = False

    def moveLeft(self):
        self.facing = 1
        self.currAcc_x = -self.baseAcc_x*self.friction

    def moveRight(self):
        self.facing = 0
        self.currAcc_x = self.baseAcc_x*self.friction

    def stop(self):
        if(self.speed_x > 1):
            self.currAcc_x = -self.baseAcc_x*self.friction
        elif(self.speed_x < -1):
            self.currAcc_x = self.baseAcc_x*self.friction
        else:
            self.speed_x = 0
            self.currAcc_x = 0

    def testPlatform(self, platform):
        if(self.x + self.rect.width > platform.get_x1() and self.x < platform.get_x2()):
            if(self.y + self.rect.height <= platform.get_y() and self.y + self.rect.height + self.speed_y >= platform.get_y()):
                self.onGround = True
                self.friction = platform.get_friction()
                self.y = platform.get_y() - self.rect.height
