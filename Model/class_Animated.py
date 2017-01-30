import pygame
from pygame.locals import *
import class_Entity

#images contient des sets d'images pour chaque animation
#states contient les états animés (ex: idle, walkLeft, walkRight ...)
class Animated(Entity):
    def __init__(self, x, y, width, height, images):
        Entity.__init__(self, x, y)
        self.rect = pygame.Rect(x, y, width, height)
        self.images = images
        self.indexImg = 0
        self.states = []
        self.states.append("idle")
        self.state = self.states[0]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def changeState(self, newState):
        oldState = self.state
        try:
            self.state = self.states.index(newState)
            indexImg = 0
            break
        except ValueError:
            self.state = oldState

    def nextImg(self):
        indexImg ++
        if(indexImg == len(self.images[self.states.index(self.state)]):
            indexImg = 0

    def get_img(self):
        return self.images[self.states.index(self.state)][indexImg]

    #Permet de mettre a jour la position de l'image a afficher
    def update(self):

    def get_rect(self):
        return self.rect
