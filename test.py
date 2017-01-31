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
from class_Atk import *
#initialisation de pygame
pygame.init()

WIDTH = 1280
HEIGHT = 720
fenetre  = pygame.display.set_mode((WIDTH,HEIGHT), RESIZABLE)

fond_e = pygame.transform.scale(pygame.image.load("Images/background.png").convert(), (1280,720))

imagesBlanchon = {
                  "RidleLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha()), True, False)
                    ],
                  "RidleRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha())
                    ],
                  "RmoveLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_0.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_2.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha()), True, False)
                    ],
                  "RmoveRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_0.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_2.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha())
                    ],
                  "FfallRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpdown_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpdown_2.png").convert_alpha())
                    ],
                  "FfallLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpdown_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpdown_2.png").convert_alpha()), True, False)
                    ],
                  "FcrouchRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_crouch_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_crouch_2.png").convert_alpha())
                    ],
                  "FcrouchLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_crouch_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_crouch_2.png").convert_alpha()), True, False)
                    ],
                  "RslideRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_slide.png").convert_alpha())
                    ],
                  "RslideLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_slide.png").convert_alpha()), True, False)
                    ],
                  "FjumpRight":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_2.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_3.png").convert_alpha())
                    ],
                  "FjumpLeft":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_2.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_jumpup_3.png").convert_alpha()), True, False)
                    ],
                  "Oaa1Right":
                    [
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_1.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_2.png").convert_alpha()),
                     pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_3.png").convert_alpha())
                    ],
                  "Oaa1Left":
                    [
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_1.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_2.png").convert_alpha()), True, False),
                     pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_3.png").convert_alpha()), True, False)
                    ]
                 }

blanchon_atkList = [Atk(2, 10, 10, {"idleRight":[pygame.image.load("Images/plateformtest.png").convert()],"idleLeft":[pygame.image.load("Images/plateformtest.png").convert()]}, 10 , 3, 0, 0, 0, 100)]
blanchon = Hero(200, 200, 64, 64, imagesBlanchon, 0.30, 0.7, 8, 6, WIDTH, 100.0, blanchon_atkList)
sol = Platform(0, HEIGHT-50, WIDTH, 10, pygame.image.load("Images/plateformtest.png").convert_alpha(), 0.4)
platform1 = Platform(80, HEIGHT-150, 100, 10, pygame.image.load("Images/plateformtest.png").convert_alpha(), 1)
platform2 = Platform(250, HEIGHT-250, 100, 10, pygame.image.load("Images/plateformtest.png").convert_alpha(), 1)
clock = pygame.time.Clock()
fps = 60
myfont = pygame.font.SysFont("monospace", 15)

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

    label = myfont.render(blanchon.get_cd(0), 1, (255,255,0))
    fenetre.blit(label, (100, 100))

    pygame.draw.rect(fenetre, (0,0,0), (blanchon.get_rect().x, blanchon.get_rect().y - 10, 62, 6))
    pygame.draw.rect(fenetre, (255,0,0), (blanchon.get_rect().x, blanchon.get_rect().y - 10,   int(max(min(blanchon.get_hp() / float(blanchon.get_hpMax()) * 60, 60), 0)),   6))

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

    blanchon.update(fps)
