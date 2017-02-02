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
class Moine(Mob):
    def __init__(self, x, y, windowWidth, strength):
        imagesMoine = {"RidleRight":[pygame.transform.scale2x(pygame.image.load("Images/Moine/m_idle_1.png").convert_alpha()),
                                     pygame.transform.scale2x(pygame.image.load("Images/Moine/m_idle_2.png").convert_alpha())],
                        "RidleLeft":[pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_idle_1.png").convert_alpha()), True, False),
                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_idle_2.png").convert_alpha()), True, False)],
                        "OdmgRight":[pygame.transform.scale2x(pygame.image.load("Images/Moine/m_dmg.png").convert_alpha())],
                        "OdmgLeft":[pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_dmg.png").convert_alpha()), True, False)],
                        "Oaa1Right":[
                                    pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk1_1.png").convert_alpha()),
                                    pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk1_2.png").convert_alpha())
                                    ],
                        "Oaa1Left":[
                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk1_1.png").convert_alpha()), True, False),
                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk1_2.png").convert_alpha()), True, False)
                                    ],
                        "Oaa2Right":[
                                    pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk2_1.png").convert_alpha()),
                                    pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk2_2.png").convert_alpha())
                                    ],
                        "Oaa2Left":[
                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk2_1.png").convert_alpha()), True, False),
                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk2_2.png").convert_alpha()), True, False)
                                    ],
                        "Oaa3Right":[
                                    pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk3_1.png").convert_alpha()),
                                    pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk3_2.png").convert_alpha()),
                                    pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk3_3.png").convert_alpha()),
                                    pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk3_4.png").convert_alpha()),
                                    ],
                        "Oaa3Left":[
                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk3_1.png").convert_alpha()), True, False),
                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk3_2.png").convert_alpha()), True, False),
                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk3_3.png").convert_alpha()), True, False),
                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atk3_4.png").convert_alpha()), True, False),
                                    ],
                        "DLeft":[
                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_dead_1.png").convert_alpha()), True, False),
                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_dead_2.png").convert_alpha()), True, False)
                                ],
                        "DRight":[
                                    pygame.transform.scale2x(pygame.image.load("Images/Moine/m_dead_1.png").convert_alpha()),
                                    pygame.transform.scale2x(pygame.image.load("Images/Moine/m_dead_2.png").convert_alpha())
                                ]}
        atkList = [Atk("violet", 2.5, 32, 16, {"idleRight":[pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atkranged1_1.png").convert_alpha()),
                                                        pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atkranged1_2.png").convert_alpha())],
                                            "idleLeft":[pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atkranged1_1.png").convert_alpha()),True,False),
                                                        pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atkranged1_2.png").convert_alpha()),True,False)]}, 8, -12, -5, 0, 6, 0, 3000),
                Atk("lazer", 3, 32, 16, {"idleRight":[pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atkranged2_1.png").convert_alpha()),
                                                    pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atkranged2_2.png").convert_alpha())],
                                        "idleLeft":[pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atkranged2_1.png").convert_alpha()),True,False),
                                                    pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atkranged2_2.png").convert_alpha()),True,False)]}, 5, 3, -1, 0, 12, 0, 3000),
                Atk("orbe", 0.1, 32, 32, {"idleRight":[pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atkranged3_1.png").convert_alpha()),
                                                        pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atkranged3_2.png").convert_alpha())],
                                            "idleLeft":[pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atkranged3_1.png").convert_alpha()),True,False),
                                                        pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Moine/m_atkranged3_2.png").convert_alpha()),True,False)]}, 12, 3, -3, 0.1, 2, -3, 4000)]

        Mob.__init__(self, x, y, 64, 64, imagesMoine, 0.2, 0.5, 2, 4, windowWidth, 200*strength, atkList)
        self.states["Oaa1Right"] = 200
        self.states["Oaa1Left"] = 200
        self.states["Oaa2Right"] = 200
        self.states["Oaa2Left"] = 200
        self.states["Oaa3Right"] = 150
        self.states["Oaa3Left"] = 150
        self.states["DRight"] = 200
        self.states["DLeft"] = 200
        self.areaWidth = 350
        self.stockOrb = 4
        self.strength = strength


    def update(self, hero, fps):
        #TODO : L'IA DU MOINE ICI
        if(self.y+self.rect.height/4.0 > hero.get_y1()):
            self.jump()
        if(self.x-self.areaWidth > hero.get_x2()):
            self.moveLeft()
            Animated.changeState(self, "RidleLeft")
        elif(self.x+self.rect.width+self.areaWidth < hero.get_x1()):
            self.moveRight()
            Animated.changeState(self, "RidleRight")
        else:
            if(abs(self.speed_x) > 0):
                self.stop()
            else:
                if(self.state[0] != 'O'):
                    if(abs(hero.get_x1() - self.x) > 300 and self.stockOrb > 0):
                        if(self.x > hero.get_x1()): #PLUIE D'ORBE SA RACE
                            Animated.changeState(self, "RidleLeft")
                            atkEffect = self.atkList[2].launch(self.x, self.y+20, -1, self.strength, -self.stockOrb)
                        else:
                            Animated.changeState(self, "RidleRight")
                            atkEffect = self.atkList[2].launch(self.x, self.y+20, 1, self.strength, self.stockOrb)
                        if(atkEffect != None):
                            self.stockOrb -= 1
                            self.atkEffectList.append(atkEffect)
                            if(self.x > hero.get_x1()):
                                Animated.changeState(self, "Oaa3Left")
                            else:
                                Animated.changeState(self, "Oaa3Right")
                    elif(hero.isOnGround() == False): #Pull violet
                        if(self.x > hero.get_x1()):
                            Animated.changeState(self, "RidleLeft")
                            atkEffect = self.atkList[0].launch(self.x, self.y+20, -1, self.strength)
                        else:
                            Animated.changeState(self, "RidleRight")
                            atkEffect = self.atkList[0].launch(self.x, self.y+20, 1, self.strength)
                        if(atkEffect != None):
                            if(self.stockOrb < 4):
                                self.stockOrb += 1
                            self.atkEffectList.append(atkEffect)
                            if(self.x > hero.get_x1()):
                                Animated.changeState(self, "Oaa1Left")
                            else:
                                Animated.changeState(self, "Oaa1Right")
                    else: #Le bon laser
                        if(self.x > hero.get_x1()):
                            Animated.changeState(self, "RidleLeft")
                            atkEffect = self.atkList[1].launch(self.x, self.y+30, -1, self.strength)
                        else:
                            Animated.changeState(self, "RidleRight")
                            atkEffect = self.atkList[1].launch(self.x, self.y+30, 1, self.strength)
                        if(atkEffect != None):
                            if(self.stockOrb < 4):
                                self.stockOrb += 4
                            self.atkEffectList.append(atkEffect)
                            if(self.x > hero.get_x1()):
                                Animated.changeState(self, "Oaa2Left")
                            else:
                                Animated.changeState(self, "Oaa2Right")

        Mob.update(self, fps)

    def set_hp(self, dmg):
        Charac.set_hp(self, dmg)
        if(self.hp <= 0.0):
            if(self.facing == 1):
                Animated.changeState(self, "DRight")
            else:
                Animated.changeState(self, "DLeft")
            self.baseJumpForce = 0
            self.speed_x = 0
            self.baseAcc_x = 0
            self.currAcc_x = 0

    def testAtkEffect(self, atkEffect):
        temp_speed_x = self.speed_x
        temp_speed_y = self.speed_y
        Charac.testAtkEffect(self, atkEffect)
        self.speed_x = temp_speed_x
        self.speed_y = temp_speed_y
