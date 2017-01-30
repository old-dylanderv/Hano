import pygame
from pygame.locals import *

#images contient des sets d'images pour chaque animation
#states contient les états animés (ex: idle, walkLeft, walkRight ...)
class Charac(Animated):
    def __init__(self, x, y, width, height, images):
        Animated.__init__(self, x, y, width, height, images)
        self.gravity = 0.25
        self.onGround = False;

    def get_x(self):
        return super.get_x()

    def get_y(self):
        return super.get_x()

    def changeState(self, newState):
        super.changeState(self, newState)

    def nextImg(self):
        super.nextImg(self)

    def display(self):
        return super.display
