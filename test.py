# -*- coding:Utf-8 -*-
#ligne permettant l'utilisateur des accents

#importation de pygame
import pygame
from pygame.locals import *
#importation de la bibliothèque system
import sys
sys.path.append('Model/')
#importation de nos classes
from class_Hero import *

#initialisation de pygame
pygame.init()

fenetre  = pygame.display.set_mode((700,530), RESIZABLE)

fond_e = pygame.image.load("Images/fondfinal.png").convert()

imagesBlanchon = [
                    [pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha())
                    ],
                    [pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_2.png").convert_alpha()),
                     #pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_3.png").convert_alpha()),
                    ]
                 ]

blanchon = Hero(200, 200, 32, 32, imagesBlanchon, 0.25, 0.5, 8, 8)

clock = pygame.time.Clock()
fps = 60

while 1 :
    clock.tick(fps)
    #boucle sur les différents événement reçut
    for event in pygame.event.get():
    	if event.type == QUIT: 			#si l'utilisateur clique sur la croix
		      sys.exit()  				#on ferme la fenêtre

    blanchon.nextImg(fps)
    fenetre.blit(fond_e, (0,0))
    fenetre.blit(blanchon.get_img(), blanchon.get_rect())

    if event.type == KEYDOWN:
    #on teste les différentes touches directionelles
    #tout en vérifiant que le personnage ne sort pas de l'écran
    #Si la touche est pressée on fait bouger le personnage
	    if event.key == K_a:
	           blanchon.changeState("atk")


    pygame.display.flip()
