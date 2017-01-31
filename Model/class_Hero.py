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
class Hero(Charac):
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
        self.combo = 1
        self.doubleJump = True
        self.jumpKeyReset = False
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.autoHit = False
        self.spell1 = False
        self.guard = False
        self.ult = False

    def key_down(self, event):
        if(event.key == K_RIGHT):
            self.right = True
        elif(event.key == K_LEFT):
            self.left = True
        elif(event.key == K_UP):
            self.up = True
        elif(event.key == K_DOWN):
            self.down = True
        elif(event.key == K_a):
            self.autoHit = True
        elif(event.key == K_z):
            self.spell1 = True
        elif(event.key == K_e):
            self.guard = True
        elif(event.key == K_r):
            self.ult = True


    def key_up(self, event):
        if(event.key == K_RIGHT):
            self.right = False
        elif(event.key == K_LEFT):
            self.left = False
        elif(event.key == K_UP):
            self.up = False
        elif(event.key == K_DOWN):
            self.down = False
        elif(event.key == K_a):
            self.autoHit = False
        elif(event.key == K_z):
            self.spell1 = False
        elif(event.key == K_e):
            self.guard = False
        elif(event.key == K_r):
            self.ult = False

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
                    if(self.speed_x > 0):
                        Animated.changeState(self, "RslideLeft")
                    else:
                        Animated.changeState(self, "RmoveLeft")
            elif(self.right == True): #Left = false && Right = true
                Charac.moveRight(self)
                if(self.onGround == True):
                    if(self.speed_x < 0):
                        Animated.changeState(self, "RslideRight")
                    else:
                        Animated.changeState(self, "RmoveRight")
            else: #pas de déplacement horizontal
                Charac.stop(self)
                if(self.onGround == True):
                    if(self.speed_x < 0):
                        Animated.changeState(self, "RslideRight")
                    elif(self.speed_x > 0):
                        Animated.changeState(self, "RslideLeft")
                    else:
                        if(self.facing == 1):
                            if(self.down == True):
                                Animated.changeState(self, "FcrouchRight")
                            else:
                                Animated.changeState(self, "RidleRight")
                        else:
                            if(self.down == True):
                                Animated.changeState(self, "FcrouchLeft")
                            else:
                                Animated.changeState(self, "RidleLeft")

            if(self.up == True):
                if(self.onGround == True):
                    Charac.jump(self)
                    self.jumpKeyReset = True
                    if(self.facing == 1):
                        Animated.changeState(self, "FjumpRight")
                    else:
                        Animated.changeState(self, "FjumpLeft")
                elif(self.doubleJump == True):
                    Charac.jump(self)
                    self.doubleJump = False
                    if(self.facing == 1):
                        Animated.changeState(self, "FjumpRight")
                    else:
                        Animated.changeState(self, "FjumpLeft")
            else: #Il faut relacher la touche de saut pour pouvoir doublesauter
                if(self.jumpKeyReset == True and self.onGround == False):
                    self.doubleJump = True
                    self.jumpKeyReset = False

            if(self.speed_y > 0):
                if(self.facing == 1):
                    Animated.changeState(self, "FfallRight")
                else:
                    Animated.changeState(self, "FfallLeft")
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
