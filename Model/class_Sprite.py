# -*- coding:Utf-8 -*-
#ligne permettant l'utilisateur des accents

#importation de pygame
import pygame
from pygame.locals import *

#Classe générique des sprites
class MySprite():
    # Constructeur, self correspond +- au 'this'
    def __init__(self, pos_x, pos_y, image, largeur, hauteur):

        # Initialisation et affectation de l'attribut image
        self.image = pygame.image.load(image).convert_alpha()

        # Initialisation et affectation de l'attribut rect
        self.rect = pygame.Rect(pos_x, pos_y, largeur, hauteur)

    # Retourne le rectangle (position)
    def get_rect(self):
        return self.rect

        # Retourne la 'surface'
    def get_img(self):
        return self.image
