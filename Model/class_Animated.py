# coding=utf-8
import pygame
from pygame.locals import *
from class_Entity import *

#images contient des sets dimages pour chaque animation
#states contient les etats animes (ex: idle, walkLeft, walkRight ...)
class Animated(Entity):
    def __init__(self, x, y, width, height, images):
        Entity.__init__(self, x, y)
        self.rect = pygame.Rect(x, y, width, height)
        self.images = images
        self.indexImg = 0
        self.states = {"idle":500, "atk":100}
        self.state = self.states.keys()[0]
        self.timerAnim = 0

    def changeState(self, newState):
        oldState = self.state
        try:
            self.state = self.states.index(newState)
            self.indexImg = 0
        except ValueError:
            self.state = oldState

    def nextImg(self, fps):
        self.timerAnim = self.timerAnim + (1000/fps)
        if self.timerAnim > self.states.get(self.state):
            self.timerAnim = self.timerAnim - self.states.get(self.state)
            self.indexImg = self.indexImg + 1
            if(self.indexImg == len(self.images[self.states.keys().index(self.state)])):
                self.indexImg = 0

    def get_img(self):
        return self.images[self.states.keys().index(self.state)][self.indexImg]

    #Permet de mettre a jour la position de l'image a afficher
    #def update(self):

    def get_rect(self):
        return self.rect
