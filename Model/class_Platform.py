# coding=utf-8
import pygame
from pygame.locals import *
from class_Animated import *

#Platform est une classe générique de plateforme (y compris le sol)
#Caractéristique de plateforme
#   self.rect correspond à la hitbox de la plateforme
#   un coefficient de frottement doit etre appliqué a qui arrive sur la plateforme
class Platform(Animated):
    def __init__(self, x, y, width, height, images, friction):
        Animated.__init__(self, x, y, width, height, images)
        self.friction = friction

    def get_friction(self):
        return self.friction

    def get_x1(self):
        return self.x

    def get_x2(self):
        return self.x + self.width

    def get_y(self):
        return self.y
