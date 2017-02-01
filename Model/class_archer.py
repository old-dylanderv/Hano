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
class Archer(Mob):
    def __init__(self, x, y, windowWidth, strength):
        imagesArcher = {"RidleRight":[pygame.transform.scale2x(pygame.image.load("Images/Archer/a_idle.png").convert_alpha())],
                        "RidleLeft":[pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Archer/a_idle.png").convert_alpha()), True, False)],
                        "OdmgRight":[pygame.transform.scale2x(pygame.image.load("Images/Archer/a_dmg_2.png").convert_alpha())],
                        "OdmgLeft":[pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Archer/a_dmg_2.png").convert_alpha()), True, False)]}
        atkList = Atk("fleche", 2, 32, 16, {"idleRight":[pygame.image.load("Images/Archer/Fleche.png").convert_alpha()],"idleLeft":[pygame.transform.flip(pygame.image.load("Images/Archer/Fleche.png").convert_alpha(),True,False)]}, 1, 3, -1, 0.1, 8, -1, 3000),
        Mob.__init__(self, x, y, 64, 64, imagesArcher, 0.3, 0.5, 5, 12, windowWidth, 50, atkList)
