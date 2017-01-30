# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *

#Charac est la classe générique des mobs, des boss et du héro
#Charac possede:
#   une vitesse (speed_x et speed_y)
#   une force de saut (baseJumpForce)
#   une poussée en x (baseAcc_x)
#   une accélération en x (currAcc_x)
#   une vitesse maximale en x
class Charac(Animated):
    def __init__(self, x, y, width, height, images, baseAcc_x, baseJumpForce, maxSpeed_x):
        Animated.__init__(self, x, y, width, height, images)
        self.gravity = 0.25
        self.onGround = False
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
        else if(self.speed_x < -self.maxSpeed_x):
            self.speed_x = -self.maxSpeed_x
        self.x += self.speed_x

        #Bloc de gestion de la vitesse en y
        if(self.onGround == True):
            self.speed_y = 0
        else:
            self.speedY += self.gravity
            self.y += self.speedY

    def jump(self):
        self.speedY = -self.baseJumpForce
        self.onGround = False

    def moveLeft(self):
        self.currAcc_x = -self.baseAcc_x

    def moveRight(self):
        self.currAcc_x = self.baseAcc_x
