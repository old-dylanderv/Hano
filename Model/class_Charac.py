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
class Charac(Animated):
    def __init__(self, x, y, width, height, images, weight, baseAcc_x, baseJumpForce, maxSpeed_x):
        Animated.__init__(self, x, y, width, height, images)
        self.weight = weight
        self.facing = 0
        self.onGround = True
        self.speed_x = 0
        self.speed_y = 0
        self.baseAcc_x = baseAcc_x
        self.currAcc_x = 0
        self.baseJumpForce = baseJumpForce
        self.maxSpeed_x = maxSpeed_x

    def update(self):
        #Bloc de gestion de la vitesse en x
        self.speed_x += self.currAcc_x
        if(self.speed_x > self.maxSpeed_x):
            self.speed_x = self.maxSpeed_x
        elif(self.speed_x < -self.maxSpeed_x):
            self.speed_x = -self.maxSpeed_x
        self.x += self.speed_x

        #Bloc de gestion de la vitesse en y
        if(self.onGround == True):
            self.speed_y = 0
        else:
            self.speed_y += self.weight
            self.y += self.speed_y
        Animated.update(self)

    def jump(self):
        self.speedY = -self.baseJumpForce
        self.onGround = False

    def moveLeft(self):
        self.facing = 1
        self.currAcc_x = -self.baseAcc_x

    def moveRight(self):
        self.facing = 0
        self.currAcc_x = self.baseAcc_x

    def stop(self):
        if(self.speed_x > 1):
            self.currAcc_x = -self.baseAcc_x
        elif(self.speed_x < -1):
            self.currAcc_x = self.baseAcc_x
        else:
            self.speed_x = 0
<<<<<<< HEAD
=======
            self.currAcc_x = 0
>>>>>>> 44de141014a5c9e6cd4caf3e88e33284e289ab27
