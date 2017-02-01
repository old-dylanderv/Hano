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
        self.states['Oaa2Right'] = 60
        self.states['Oaa2Left'] = 60
        self.states['Oaa3Right'] = 50
        self.states['Oaa3Left'] = 50
        self.autoHitTimer2 = 0 #Sert à transformer l'auto hit 1 apres un coup reussi
        self.autoHitTimer3 = 0 #Sert à transformer l'auto hit 2 apres un coup reussi
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

    def get_combo(self):
        return self.combo

    def update(self, fps):
        #BLOC GESTION MOUVEMENT -----------------------------------
        if(self.state[0] == 'O'): #Pas de mouvement ni d'attaque si le personnage est en animation one time
            if(self.isFirstFrame() == True):
                self.speed_x = 0
                self.currAcc_x = 0
                self.speed_y = 0
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
                if(self.autoHitTimer2 > 0): #Le joueur peut declencher l'auto hit 2
                    if(self.facing == 1):
                        atkEffect = self.atkList[1].launch(self.x+self.rect.width, self.y+20, self.facing, self.combo)
                    else:
                        atkEffect = self.atkList[1].launch(self.x-self.atkList[0].get_width(), self.y+20, self.facing, self.combo)
                    if(atkEffect != None):
                        self.autoHitTimer2 = 0
                        self.atkEffectList.append(atkEffect)
                        if(self.facing == 1):
                            Animated.changeState(self, "Oaa2Right")
                        else:
                            Animated.changeState(self, "Oaa2Left")
                elif(self.autoHitTimer3 > 0): #Le joueur peut declencher l'auto hit 3
                    if(self.facing == 1):
                        self.speed_x = 5
                        self.speed_y = -2
                        atkEffect = self.atkList[2].launch(self.x+self.rect.width, self.y+20, self.facing, self.combo, self.speed_x)
                    else:
                        self.speed_x = -5
                        self.speed_y = -2
                        atkEffect = self.atkList[2].launch(self.x-self.atkList[0].get_width(), self.y+20, self.facing, self.combo, self.speed_x)
                    if(atkEffect != None):
                        self.autoHitTimer3 = 0
                        self.atkEffectList.append(atkEffect)
                        if(self.facing == 1):
                            Animated.changeState(self, "Oaa3Right")
                        else:
                            Animated.changeState(self, "Oaa3Left")
                else: #Le joueur declenche l'auto hit 1
                    if(self.facing == 1):
                        atkEffect = self.atkList[0].launch(self.x+self.rect.width, self.y+20, self.facing, self.combo)
                    else:
                        atkEffect = self.atkList[0].launch(self.x-self.atkList[0].get_width(), self.y+20, self.facing, self.combo)
                    if(atkEffect != None):
                        self.atkEffectList.append(atkEffect)
                        if(self.facing == 1):
                            Animated.changeState(self, "Oaa1Right")
                        else:
                            Animated.changeState(self, "Oaa1Left")
            if(self.spell1 == True):
                if(self.facing == 1):
                    atkEffect = self.atkList[3].launch(self.x+self.rect.width/2+20*self.facing, self.y+20, self.facing, self.combo, self.speed_x)
                else:
                    atkEffect = self.atkList[3].launch(self.x+self.rect.width/2+20*self.facing-self.atkList[0].get_width(), self.y+20, self.facing, self.combo, self.speed_x)
                if(atkEffect != None):
                    self.atkEffectList.append(atkEffect)
                    if(self.facing == 1):
                        Animated.changeState(self, "Oaa1Right")
                    else:
                        Animated.changeState(self, "Oaa1Left")
                    self.atkList[0].put_on_cd() #Si le coup de pied est lance on met un cd sur le coup de poing

        if(self.autoHitTimer2 > 0):
            self.autoHitTimer2 = self.autoHitTimer2 - (1000.0/fps)

        if(self.autoHitTimer3 > 0):
            self.autoHitTimer3 = self.autoHitTimer3 - (1000.0/fps)

        Charac.update(self, fps)

    #Ici on peut vérifier si l'atk i à touché quelqu'un avant de la suppr
    def deleteAtkEffect(self, i):
        if(self.atkEffectList[i].didHit() == True): #L'attaque a touché
            self.comboManager(self.atkEffectList[i].get_nom())
        Charac.deleteAtkEffect(self, i)

    def comboManager(self, attName):
        if(attName == "autoHit1"):
            self.combo += 0.1
            self.autoHitTimer2 = 2000
            self.atkList[1].put_on_cd()
        elif(attName == "autoHit2"):
            self.combo += 0.2
            self.autoHitTimer2 = 0
            self.autoHitTimer3 = 2000
            self.atkList[2].put_on_cd()
        elif(attName == "autoHit3"):
            self.combo += 0.4
            self.autoHitTimer2 = 0
            self.autoHitTimer3 = 0
        elif(attName == "EOF"):
            self.combo += 0.1


    def giveDoubleJump(self):
        self.doubleJump = True
