# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *

#images contient des sets d'images pour chaque animation
#states contient les états animés (ex: idle, walkLeft, walkRight ...)
class Charac(Animated):
    def __init__(self, x, y, width, height, images):
        Animated.__init__(self, x, y, width, height, images)
        self.gravity = 0.25
        self.onGround = False;
