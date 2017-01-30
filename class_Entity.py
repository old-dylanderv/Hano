import pygame
from pygame.locals import *

class Entity():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_img(self):
        return self.img
