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

    def update(self, fps):
        #BLOC GESTION MOUVEMENT -----------------------------------
        if(self.state[0] == 'O'): #Pas de mouvement ni d'attaque si le personnage est en animation one time
            speed_x = 0
            speed_y = 0
        else:
            #Left = true && Right = false
            if(self.left == True and self.right == False):
                Charac.moveLeft(self)
                if(self.onGround == True):
                    Animated.changeState(self, "RmoveLeft")
            elif(self.right == True): #Left = false && Right = true
                Charac.moveRight(self)
                if(self.onGround == True):
                    Animated.changeState(self, "RmoveRight")
            else: #pas de déplacement horizontal
                Charac.stop(self)
                if(self.onGround == True):
                    Animated.changeState(self, "RslideLeft")
                    else:
                        if(self.facing == 1):
                            Animated.changeState(self, "RidleRight")
                        else:
                            Animated.changeState(self, "RidleLeft")

            if(self.up == True):
                if(self.onGround == True):
                    Charac.jump(self)
                    if(self.facing == 1):
                        Animated.changeState(self, "FjumpRight")
                    else:
                        Animated.changeState(self, "FjumpLeft")

            #BLOC GESTION SPELL -------------------------------------
            if(self.autoHit == True):
                if(self.atkList[0].launch(self.x+self.rect.width/2+20*self.facing, self.y+20, self.facing, self.combo) != None):
                    if(self.facing == 1):
                        Animated.changeState(self, "Oaa1Right")
                    else:
                        Animated.changeState(self, "Oaa1Left")

        Charac.update(self, fps)

    def giveDoubleJump(self):
        self.doubleJump = True
