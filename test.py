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
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_3.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_2.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_3.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_4.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_5.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_2.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_3.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_4.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_5.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_6.png").convert_alpha())
                    ]
                 ]

blanchon = Hero(200, 200, 32, 32, imagesBlanchon, 0.25, 0.5, 8, 8)

clock = pygame.time.Clock()
fps = 60
myfont = pygame.font.SysFont("monospace", 15)

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
		blanchon.key_down(event)
    if event.type == KEYUP:
		blanchon.key_up(event)

    label = myfont.render(str(blanchon.getKeyLeft()), 1, (255,255,0))
    fenetre.blit(label, (100, 100))
    label1 = myfont.render(str(blanchon.getKeyRight()), 1, (255,255,0))
    fenetre.blit(label1, (200, 100))

    pygame.display.flip()
    blanchon.update()
