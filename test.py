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
from class_Platform import *
#initialisation de pygame
pygame.init()

WIDTH = 1000
HEIGHT = 650
fenetre  = pygame.display.set_mode((WIDTH,HEIGHT), RESIZABLE)

fond_e = pygame.image.load("Images/fondfinal.png").convert()

imagesBlanchon = {
                  "idleLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha()), True, False)
                    ],
                  "idleRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha())
                    ],
                  "moveLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_0.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_2.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha()), True, False)
                    ],
                  "moveRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_0.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_2.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha())
                    ],
                  "fallRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha())
                    ],
                  "fallLeft":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha())
                    ],
                  "crouchRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha())
                    ],
                  "crouchLeft":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha())
                    ],
                  "slideRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha())
                    ],
                  "slideLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha()), True, False)
                    ],
                  "jumpRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_2.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_3.png").convert_alpha())
                    ],
                  "jumpLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha()), True, False)
                    ]
                 }

imagePlateform = {
                    "idleLeft":
                      [
                       pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()), True, False),
                       pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha()), True, False)
                      ],
                    "idleRight":
                      [
                       pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()),
                       pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha())
                      ]
                 }



blanchon = Hero(200, 200, 64, 64, imagesBlanchon, 0.25, 0.5, 8, 8, WIDTH)
sol = Platform(0, HEIGHT, WIDTH, 10, imagePlateform, 1)
platform1 = Platform(50, HEIGHT-100, 100, 10, imagePlateform, 1)
platform2 = Platform(200, HEIGHT-200, 100, 10, imagePlateform, 1)
clock = pygame.time.Clock()
fps = 60
myfont = pygame.font.SysFont("monospace", 15)
img = pygame.Surface((50,430))

#Quand on glisse et qu'on saute, le perso se deplace dans la direction de la glissade

while 1 :
    clock.tick(fps)
    #boucle sur les différents événement reçut
    for event in pygame.event.get():
        if event.type == QUIT: 	#si l'utilisateur clique sur la croix
            sys.exit()          #on ferme la fenêtre
        if event.type == KEYDOWN:
            blanchon.key_down(event)
        if event.type == KEYUP:
            blanchon.key_up(event)

    blanchon.nextImg(fps)
    fenetre.blit(fond_e, (0,0))
    fenetre.blit(blanchon.get_img(), blanchon.get_rect())
    fenetre.blit(platform1.get_img(), platform1.get_rect())
    fenetre.blit(platform2.get_img(), platform2.get_rect())

    #INFO TEST
    label = myfont.render("double jump = "+str(blanchon.getDoubleJump()), 1, (255,255,0))
    fenetre.blit(label, (10, 10))
    label1 = myfont.render("State = "+str(blanchon.get_state()), 1, (255,255,0))
    fenetre.blit(label1, (10, 30))

    pygame.display.flip()
    #Servira a tester si le joueur est descendu d'une plateforme
    heroOnGround = blanchon.isOnGround()

    blanchon.setOnAir()
    blanchon.testPlatform(sol)
    blanchon.testPlatform(platform1)
    blanchon.testPlatform(platform2)

    #Le hero est descendu d'une plateforme
    if(heroOnGround == True and blanchon.isOnGround() == False):
        blanchon.giveDoubleJump() #On lui donne un saut

    blanchon.update()
