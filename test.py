# -*- coding:Utf-8 -*-
#ligne permettant l'utilisateur des accents

#importation de pygame
import pygame
from pygame.locals import *
#importation de la bibliothèque system
import sys
#importation de nos classes
from Model/class_Animated import *

#initialisation de pygame
pygame.init()

fenetre  = pygame.display.set_mode((700,530), RESIZABLE)

fond_e = pygame.image.load("Images/fondfinal.png").convert()

blanchon = Animated(200, 200, ("Images/b_stop_1.png","Images/b_stop_2.png"))

while 1
    
