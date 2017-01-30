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
        self.states['moveLeft'] = 100
        self.states['moveRight'] = 100
        self.states['jumpLeft'] = 50
        self.states['jumpRight'] = 50
        self.states['fallLeft'] = 100
        self.states['fallRight'] = 100
        self.states['slideLeft'] = 50
        self.states['slideRight'] = 50
        self.states['crouchLeft'] = 50
        self.states['crouchRight'] = 50
        self.doubleJump = True
        self.up = False
        self.down = False
        self.left = False
        self.right = False

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
        #Left = true && Right = false
        if(self.left == True and self.right == False):
            Charac.moveLeft(self)
            if(self.speed_x > 0):
                Animated.changeState(self, "slideLeft")
            else:
                Animated.changeState(self, "moveLeft")
        elif(self.right == True): #Left = false && Right = true
            Charac.moveRight(self)
            if(self.speed_x < 0):
                Animated.changeState(self, "slideRight")
            else:
                Animated.changeState(self, "moveRight")
        elif(self.up == False and self.down == False): #pas de déplacement
            Charac.stop(self)
            if(self.speed_x < 0):
                Animated.changeState(self, "slideRight")
            elif(self.speed_x > 0):
                Animated.changeState(self, "slideLeft")
            else:
                if(self.facing == 0):
                    Animated.changeState(self, "idleRight")
                else:
                    Animated.changeState(self, "idleLeft")

        if(self.up == True):
            if(self.onGround == True):
                Charac.jump(self)
                if(self.facing == 0):
                    Animated.changeState(self, "jumpRight")
                else:
                    Animated.changeState(self, "jumpLeft")
            elif(self.doubleJump == True):
                Charac.jump(self)
                if(self.facing == 0):
                    Animated.changeState(self, "jumpRight")
                else:
                    Animated.changeState(self, "jumpLeft")
                self.doubleJump = False

        if(self.y < 0):
            if(self.facing == 0):
                Animated.changeState(self, "fallRight")
            else:
                Animated.changeState(self, "fallLeft")

        Charac.update(self)

    def getKeyRight(self):
        return self.right

    def getKeyLeft(self):
        return self.left
