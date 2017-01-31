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
        self.states = {}
        self.states["idleLeft"] = 500
        self.states["idleRight"] = 500
        self.state = self.states.keys()[0]
        self.timerAnim = 0

    def changeState(self, newState):
        if(newState != self.state):
            oldState = self.state
            try:
                self.state = self.states.keys()[self.states.keys().index(newState)]
                self.indexImg = 0
                print(newState+" est pas dans la pool de states")
            except ValueError:
                self.state = oldState
                print(newState+" n'est pas dans la pool de states")

    def nextImg(self, fps):
        self.timerAnim = self.timerAnim + (1000/fps)
        timeState = self.states.get(self.state)
        if self.timerAnim > timeState:
            self.timerAnim = self.timerAnim - timeState
            self.indexImg = self.indexImg + 1
            if(self.indexImg == len(self.images.get(self.state))):
                self.indexImg = 0

    def get_img(self):
        return self.images.get(self.state)[self.indexImg]

    #Permet de mettre a jour la position de l'image a afficher
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def get_rect(self):
        return self.rect
