# -*- coding:Utf-8 -*-
#ligne permettant l'utilisateur des accents

#importation de pygame
import pygame
from pygame.locals import *
#importation de la bibliothèque system
import sys
#importation de nos classes
from class_Animated import *

#initialisation de pygame
pygame.init()

fenetre  = pygame.display.set_mode((700,530), RESIZABLE)

fond_e = pygame.image.load("Images/fondfinal.png").convert()

imagesBlanchon = ( (pygame.image.load("Images/b_stop_1.png").convert_alpha(), pygame.image.load("Images/b_stop_2.png").convert_alpha()) )

blanchon = Animated(200, 200, 32, 32, imagesBlanchon)


while 1 :
    #boucle sur les différents événement reçut
    for event in pygame.event.get():
    	if event.type == QUIT: 			#si l'utilisateur clique sur la croix
		      sys.exit()  				#on ferme la fenêtre

    fenetre.blit(blanchon.self.get_rect, blanchon.get_img())
