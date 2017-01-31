# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
from class_Entity import *

class Atk(Entity):
    def __init__(self, x, y, dmg, cd, knockback):
        Entity.__init__(self, x, y)
        self.dmg = dmg
        self.cd = cd
        self.timer = 0
        self.knockback = knockback

    def launch(self):
