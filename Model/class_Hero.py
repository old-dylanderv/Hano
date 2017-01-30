# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
from class_Charac import *
#Hero est la classe générique des héros
#Carastéristiques des héros:
#   Ils sont controlés au clavier
#   Ils peuvent double-sauter
#   Ils ont des spells (définis dans la classe fille)
class Hero(Charac):
    def __init__(self, x, y, width, height, images, weight, baseAcc_x, baseJumpForce, maxSpeed_x):
        Charac.__init__(self, x, y, width, height, images, weight, baseAcc_x, baseJumpForce, maxSpeed_x)
        self.doubleJump = true

    def input(self, event):
        if(event.key == K_RIGHT):
            self.moveRight()
        elif(event.key == K_LEFT):
            self.moveLeft()
        elif(event.key == K_UP):
            if(self.onGround == True):
                self.jump()
            elif(self.doubleJump == True):
                self.jump()
                self.doubleJump = False

    #def update(self):

    #def jump(self):

    #def moveLeft(self):

    #def moveRight(self):
