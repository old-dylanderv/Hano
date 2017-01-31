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
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpdown_2.png").convert_alpha())
                    ],
                  "fallLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpdown_2.png").convert_alpha()), True, False),
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
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_slide.png").convert_alpha())
                    ],
                  "slideLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_slide.png").convert_alpha()), True, False)
                    ],
                  "jumpRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_3.png").convert_alpha())
                    ],
                  "jumpLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_3.png").convert_alpha()), True, False)
                    ]
                 }

blanchon = Hero(200, 200, 64, 64, imagesBlanchon, 0.30, 0.7, 8, 6, WIDTH, 100.0)
sol = Platform(0, HEIGHT, WIDTH, 10, pygame.image.load("Images/plateformtest.png").convert_alpha(), 0.4)
platform1 = Platform(50, HEIGHT-100, 100, 10, pygame.image.load("Images/plateformtest.png").convert_alpha(), 1)
platform2 = Platform(200, HEIGHT-200, 100, 10, pygame.image.load("Images/plateformtest.png").convert_alpha(), 1)
clock = pygame.time.Clock()
fps = 60

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
    fenetre.blit(sol.get_img(), sol.get_rect())
    fenetre.blit(platform1.get_img(), platform1.get_rect())
    fenetre.blit(platform2.get_img(), platform2.get_rect())

    pygame.draw.rect(fenetre, (255,0,0), (50,  50,   int(max(min(blanchon.get_hp() / float(blanchon.get_hpMax()) * 200, 200), 0)),   10))

    blanchon.set_hp(0.2)

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
