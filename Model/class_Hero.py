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
        self.up = False;
        self.down = False;
        self.left = False;
        self.right = False;

    def key_down(self, event):
        if(event.key == K_RIGHT):
            self.right = True
        elif(event.key == K_LEFT):
            self.left = True
        elif(event.key == K_UP):
            self.up = True
        elif(event.key == K_DOWN):
            self.down = True

    def key_up(self, event):
        if(event.key == K_RIGHT):
            self.right = False
        elif(event.key == K_LEFT):
            self.left = False
        elif(event.key == K_UP):
            self.up = False
        elif(event.key == K_DOWN):
            self.down = False

    def update(self):
        if(self.left == True and self.right == True):
            Charac.moveLeft(self)
        elif(self.right == True):
            Charac.moveRight(self)
        elif(self.up == False and self.down == False):
            Charac.stop(self)

        if(self.up == True):
            if(self.onGround == True):
                Charac.jump(self)
            elif(self.doubleJump == True):
                Charac.jump(self)
                self.doubleJump = False

        Charac.update(self)
