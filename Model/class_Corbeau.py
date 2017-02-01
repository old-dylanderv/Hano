# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
from class_Mob import *
from class_Atk import *
from class_AtkEffect import *
#Hero est la classe générique des héros
#Carastéristiques des héros:
#   Ils sont controlés au clavier
#   Ils peuvent double-sauter
#   Ils ont des spells (définis dans la classe fille)
class Corbeau(Mob):
    def __init__(self, x, y, windowWidth, strength):
        imagesCorbeau = {"RidleRight":[pygame.transform.scale2x(pygame.image.load("Images/Corbeau/c_fly_1.png").convert_alpha()),
                                        pygame.transform.scale2x(pygame.image.load("Images/Corbeau/c_fly_2.png").convert_alpha())],
                        "RidleLeft":[pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Corbeau/c_fly_1.png").convert_alpha()), True, False),
                                        pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Corbeau/c_fly_2.png").convert_alpha()), True, False)],
                        "RmoveRight":[pygame.transform.scale2x(pygame.image.load("Images/Corbeau/c_fly_1.png").convert_alpha()),
                                    pygame.transform.scale2x(pygame.image.load("Images/Corbeau/c_fly_2.png").convert_alpha())],
                        "RmoveLeft":[pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Corbeau/c_fly_1.png").convert_alpha()), True, False),
                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Corbeau/c_fly_2.png").convert_alpha()), True, False)],
                        "OdmgRight":[pygame.transform.scale2x(pygame.image.load("Images/Corbeau/c_dmg.png").convert_alpha())],
                        "OdmgLeft":[pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Corbeau/c_dmg.png").convert_alpha()), True, False)]}
        atkList = Atk("shuriken", 3, 16, 16, {"idleLeft":[pygame.image.load("Images/Corbeau/shuriken.png").convert_alpha()],"idleRight":[pygame.transform.flip(pygame.image.load("Images/Corbeau/shuriken.png").convert_alpha(),True,False)]}, 2, 3, 1, 0.3, 0, 2, 2000),
        Mob.__init__(self, x, y, 32, 32, imagesCorbeau, 0.01, 1, 1, 8, windowWidth, 10*strength, atkList)
        self.strength = strength
        self.min_y = (pygame.time.get_ticks()%200) + 100
        self.left = True
        self.right = False

    def update(self, hero, fps):
        #TODO : L'IA DU CORBEAU ICI
        if(self.y > self.min_y):
            self.jump()
        if(self.left == True):
            self.moveLeft()
            Animated.changeState(self, "RmoveLeft")
        else:
            self.moveRight()
            Animated.changeState(self, "RmoveRight")

        if(self.x < 50 and self.left == True):
            self.left = False
            self.right = True
        elif(self.x+self.rect.width > self.windowWidth - 50 and self.right == True):
            self.left = True
            self.right = False

        atkEffect = self.atkList[0].launch(self.x+self.rect.width/2, self.y+self.rect.height, 1, self.strength, self.speed_x)
        if(atkEffect != None):
            self.atkEffectList.append(atkEffect)

        Mob.update(self, fps)
