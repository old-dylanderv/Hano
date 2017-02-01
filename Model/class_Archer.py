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
class Archer(Mob):
    def __init__(self, x, y, windowWidth, strength):
        imagesArcher = {"RidleRight":[pygame.transform.scale2x(pygame.image.load("Images/Archer/a_idle.png").convert_alpha())],
                        "RidleLeft":[pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Archer/a_idle.png").convert_alpha()), True, False)],
                        "OdmgRight":[pygame.transform.scale2x(pygame.image.load("Images/Archer/a_dmg_2.png").convert_alpha())],
                        "OdmgLeft":[pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Archer/a_dmg_2.png").convert_alpha()), True, False)],
                        "Oaa1Right":[
                                        pygame.transform.scale2x(pygame.image.load("Images/Archer/a_atk_1.png").convert_alpha()),
                                        pygame.transform.scale2x(pygame.image.load("Images/Archer/a_atk_2.png").convert_alpha()),
                                        pygame.transform.scale2x(pygame.image.load("Images/Archer/a_atk_3.png").convert_alpha()),
                                        pygame.transform.scale2x(pygame.image.load("Images/Archer/a_atk_4.png").convert_alpha())
                                    ],
                        "Oaa1Left":[
                                        pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Archer/a_atk_1.png").convert_alpha()), True, False),
                                        pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Archer/a_atk_2.png").convert_alpha()), True, False),
                                        pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Archer/a_atk_3.png").convert_alpha()), True, False),
                                        pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Archer/a_atk_4.png").convert_alpha()), True, False)
                                    ],
                        "RmoveRight":[
                                        pygame.transform.scale2x(pygame.image.load("Images/Archer/a_move_1.png").convert_alpha()),
                                        pygame.transform.scale2x(pygame.image.load("Images/Archer/a_move_2.png").convert_alpha()),
                                        pygame.transform.scale2x(pygame.image.load("Images/Archer/a_move_3.png").convert_alpha())
                                    ],
                        "RmoveLeft":[
                                        pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Archer/a_move_1.png").convert_alpha()), True, False),
                                        pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Archer/a_move_2.png").convert_alpha()), True, False),
                                        pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Archer/a_move_3.png").convert_alpha()), True, False)
                                    ]}
        atkList = Atk("fleche", 2.5, 32, 16, {"idleLeft":[pygame.image.load("Images/Archer/Fleche.png").convert_alpha()],"idleRight":[pygame.transform.flip(pygame.image.load("Images/Archer/Fleche.png").convert_alpha(),True,False)]}, 2, 3, -1, 0.05, 15, -1, 3000),
        Mob.__init__(self, x, y, 64, 64, imagesArcher, 0.2, 1, 5, 10, windowWidth, 20*strength, atkList)
        self.strength = strength
        self.arrowMax = 3 + int(strength)
        self.arrowCount = 0
        self.flee_x = 0
        self.flee_set = False

    def update(self, hero, fps):
        #TODO : L'IA DE L'ARCHER ICI
        if(self.flee_set == True):
            if(self.x-30 > self.flee_x):
                Animated.changeState(self, "RmoveLeft")
                self.moveLeft()
            elif(self.x+30 < self.flee_x):
                Animated.changeState(self, "RmoveRight")
                self.moveRight()
            else:
                self.flee_set = False
                self.arrowCount = 0
        else:
            if(abs(self.speed_x) > 0):
                self.stop()
            else:
                if(self.state[0] != 'O'):
                    if(self.arrowCount < self.arrowMax):
                        if(self.x > hero.get_x2()):
                            Animated.changeState(self, "RidleLeft")
                            atkEffect = self.atkList[0].launch(self.x+self.rect.width, self.y+20, -1, self.strength)
                        else:
                            Animated.changeState(self, "RidleRight")
                            atkEffect = self.atkList[0].launch(self.x-self.atkList[0].get_width(), self.y+20, 1, self.strength)
                        if(atkEffect != None):
                            self.atkEffectList.append(atkEffect)
                            self.arrowCount += 1
                            if(self.x > hero.get_x2()):
                                Animated.changeState(self, "Oaa1Left")
                            else:
                                Animated.changeState(self, "Oaa1Right")
                    else:
                        self.flee_set = True
                        self.flee_x = (self.x+pygame.time.get_ticks()%(self.windowWidth))%(self.windowWidth-self.rect.width-200)+100

        Mob.update(self, fps)
