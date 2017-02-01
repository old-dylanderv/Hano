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
class Ninja(Mob):
    def __init__(self, x, y, windowWidth, strength):
        imagesNinja = {"RidleLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_idle_1.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_idle_2.png").convert_alpha()), True, False)
                        ],
                      "RidleRight":
                        [
                         pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_idle_1.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_idle_2.png").convert_alpha())
                        ],
                      "RmoveLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_1.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_mv.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_1.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_mv.png").convert_alpha()), True, False)
                        ],
                      "RmoveRight":
                        [
                         pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_1.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_mv.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_1.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_mv.png").convert_alpha()),
                        ],
                       "Oaa1Left":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_1.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_2.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_3.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_4.png").convert_alpha()), True, False),
                        ],
                        "Oaa1Right":
                         [
                          pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_1.png").convert_alpha()),
                          pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_2.png").convert_alpha()),
                          pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_3.png").convert_alpha()),
                          pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_4.png").convert_alpha()),
                         ],
                        "OdmgRight":
                         [
                          pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_hurt.png").convert_alpha()),
                         ],
                         "OdmgLeft":
                         [
                          pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_hurt.png").convert_alpha()), True, False),
                         ]
                     }
        atkList = Atk("sabre", 3, 64, 32, {"idleLeft":[pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha()],"idleRight":[pygame.transform.flip(pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha(),True,False)]}, 10, 10, -4, 0, 4, 0, 400),
        Mob.__init__(self, x, y, 64, 64, imagesNinja, 0.2, 2, 8, 12, windowWidth, 30*strength, atkList)
        self.strength = strength
        self.areaWidth = 200

    def update(self, hero, fps):
        #TODO : L'IA DU NINJA ICI
        if(self.x-self.areaWidth > hero.get_x2()):
            self.moveLeft()
            Animated.changeState(self, "RmoveLeft")
        elif(self.x+self.rect.width+self.areaWidth < hero.get_x1()):
            self.moveRight()
            Animated.changeState(self, "RmoveRight")
        else:
            if(abs(self.speed_x) > 0):
                self.stop()
            else:
                if(self.state[0] != 'O'):
                    if(self.x > hero.get_x1()):
                        Animated.changeState(self, "RidleLeft")
                        atkEffect = self.atkList[0].launch(self.x, self.y+20, -1, self.strength)
                    else:
                        Animated.changeState(self, "RidleRight")
                        atkEffect = self.atkList[0].launch(self.x, self.y+20, 1, self.strength)
                    if(atkEffect != None):
                        self.atkEffectList.append(atkEffect)
                        if(self.x > hero.get_x1()):
                            Animated.changeState(self, "Oaa1Left")
                        else:
                            Animated.changeState(self, "Oaa1Right")

        Mob.update(self, fps)
