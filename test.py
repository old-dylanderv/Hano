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
from class_Mob import *
from class_Archer import *
#initialisation de pygame
def main(self):
    pygame.init()

    WIDTH = 1280
    HEIGHT = 720
    fenetre  = pygame.display.set_mode((WIDTH,HEIGHT), RESIZABLE)

    fond_e = pygame.transform.scale(pygame.image.load("Images/Background/niveauRecurciforce.png").convert(), (1280,720))

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
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_3.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_3.png").convert_alpha())
                        ],
                      "Oaa1Left":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_1.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_2.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_3.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_3.png").convert_alpha()), True, False)
                        ],
                      "Oaa2Right":
                        [
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_1.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_2.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_3.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_4.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_5.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_5.png").convert_alpha())
                        ],
                      "Oaa2Left":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_1.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_2.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_3.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_4.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_5.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_5.png").convert_alpha()), True, False)
                        ],
                      "Oaa3Right":
                        [
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_1.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_2.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_3.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_4.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_5.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_6.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_6.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_6.png").convert_alpha())
                        ],
                      "Oaa3Left":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_1.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_2.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_3.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_4.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_5.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_6.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_6.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_6.png").convert_alpha()), True, False)
                        ],
                      "OaaaRight":
                        [
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_2.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_atkjumpdown.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_atkjumpdown.png").convert_alpha())
                        ],
                      "OaaaLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_2.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_atkjumpdown.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_atkjumpdown.png").convert_alpha()), True, False)
                        ]
                     }

    blanchon_atkList = [
                        Atk("autoHit1", 0.5, 32, 32, {"idleRight":[pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha()],"idleLeft":[pygame.transform.flip(pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha(),True,False)]}, 1, 5, -1, 0, 0, 0, 225),
                        Atk("autoHit2", 0.7, 32, 32, {"idleRight":[pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha()],"idleLeft":[pygame.transform.flip(pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha(),True,False)]}, 5, 5, -2, 0, 0, 0, 300),
                        Atk("autoHit3", 0.7, 32, 32, {"idleRight":[pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha()],"idleLeft":[pygame.transform.flip(pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha(),True,False)]}, 2, 6, -16, 0, 0, 0, 500),
                        Atk("EOF", 3, 32, 17, {"idleRight":[pygame.image.load("Images/Blanchon/vector.png").convert_alpha()],"idleLeft":[pygame.transform.flip(pygame.image.load("Images/Blanchon/vector.png").convert_alpha(),True,False)]}, 10 , 4, -1, 0, 4, 0, 2000),
                        Atk("airAutoHit", 1, 32, 32, {"idleRight":[pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha()],"idleLeft":[pygame.transform.flip(pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha(),True,False)]}, 5, 5, 5, 0, 0, 0, 300)
                       ]
    blanchon = Hero(200, 200, 64, 64, imagesBlanchon, 0.3, 0.7, 8, 6, WIDTH, 100.0, blanchon_atkList)
    sol = Platform(0, HEIGHT-50, WIDTH, 10, pygame.image.load("Images/plateformtest.png").convert_alpha(), 0.4)
    #INIT PLATEFORMES
    platforms = []
    platforms.append(Platform(80, HEIGHT-150, 100, 10, pygame.image.load("Images/plateform.png").convert_alpha(), 1))
    platforms.append(Platform(250, HEIGHT-250, 100, 10, pygame.image.load("Images/plateform.png").convert_alpha(), 1))

    #INIT ENNEMIS
    foes = []
    foes.append(Archer(500, 500, WIDTH, 1))
    foes.append(Archer(600, 500, WIDTH, 1))

    #INIT SYSTEM CLOCK
    clock = pygame.time.Clock()
    fps = 60
    myfont = pygame.font.SysFont("monospace", 15)

    while 1 :
        clock.tick(fps)
    #GESTION EVENT------------------------------------------------------------------
        for event in pygame.event.get():
            if event.type == QUIT: 	#si l'utilisateur clique sur la croix
                sys.exit()          #on ferme la fenêtre
            if event.type == KEYDOWN:
                blanchon.key_down(event)
            if event.type == KEYUP:
                blanchon.key_up(event)

    #GESTION DU DECORS--------------------------------------------------------------
        #Fond
        fenetre.blit(fond_e, (0,0))

        #Plateformes
        nbPlatf = len(platforms)
        for i in range (0, nbPlatf):
            fenetre.blit(platforms[i].get_img(), platforms[i].get_rect())

    #GESTION DU HERO----------------------------------------------------------------
        #Affichage Multiplicateur de dégats
        CountAH = myfont.render(u"Multiplicateur de dégats : "+str(blanchon.get_combo()), 1, (255,255,0))
        fenetre.blit(CountAH, (700, 680))

        #CoolDown Attaque de Blanchon
        if blanchon.get_onGround() == False:
            cd = blanchon_atkList[4].get_cd()
            if cd <= 0.00:
                CdAH = myfont.render(u"Coup Aérien : 0", 1, (255,255,0))
            else:
                CdAH = myfont.render(u"Coup Aérien : "+cd, 1, (255,255,0))
        elif blanchon.get_autoHitTimer3() > 0:
            CdAH = myfont.render(u"Coup de pied : "+str("{0:.1f}".format(blanchon.get_autoHitTimer3()/1000)), 1, (255,255,0))
        elif blanchon.get_autoHitTimer2() > 0:
            CdAH = myfont.render(u"Coup d'épée : "+str("{0:.1f}".format(blanchon.get_autoHitTimer2()/1000)), 1, (255,255,0))
        else:
            cd = blanchon_atkList[0].get_cd()
            if cd <= 0.00:
                CdAH = myfont.render(u"Coup de poing : 0", 1, (255,255,0))
            else:
                CdAH = myfont.render(u"Coup de poing : "+cd, 1, (255,255,0))

        fenetre.blit(CdAH, (100, 680))
        CdProj = myfont.render(u"End Of File : "+str(blanchon_atkList[3].get_cd()), 1, (255,255,0))
        fenetre.blit(CdProj, (300, 680))
        #Teste Hero => Plateforme
        heroOnGround = blanchon.isOnGround()
        blanchon.setOnAir()
        blanchon.testPlatform(sol)
        for i in range (0, nbPlatf):
            blanchon.testPlatform(platforms[i])

        #Le hero est descendu d'une plateforme
        if(heroOnGround == True and blanchon.isOnGround() == False):
            blanchon.giveDoubleJump() #On lui donne un saut

        blanchon.update(fps)

    #GESTION DES MOBS---------------------------------------------------------------

        #Teste Mob => Plateforme && Atk Hero => Mob
        nbAtkHero = len(blanchon.get_AtkEffectList())
        i = 0
        while i < len(foes):
            foes[i].nextImg(fps)
            fenetre.blit(foes[i].get_img(), foes[i].get_rect())
            pygame.draw.rect(fenetre, (0,0,0), (foes[i].get_rect().x, foes[i].get_rect().y - 10, 60, 6))
            pygame.draw.rect(fenetre, (255,0,0), (foes[i].get_rect().x, foes[i].get_rect().y - 10,   int(max(min(foes[i].get_hp() / float(foes[i].get_hpMax()) * 60, 60), 0)),   6))
            EnnemyOnGround = foes[i].isOnGround()
            foes[i].setOnAir()
            foes[i].testPlatform(sol)

            for j in range (0, nbPlatf):
                foes[i].testPlatform(platforms[j])

            #Check si le mob i se fait toucher par l'atk de hero k
            for k in range (0, nbAtkHero):
                fenetre.blit(blanchon.get_AtkEffectList()[k].get_img(), blanchon.get_AtkEffectList()[k].get_rect())
                foes[i].testAtkEffect(blanchon.get_AtkEffectList()[k])

            nbAtkFoe = len(foes[i].get_AtkEffectList())
            for l in range (0, nbAtkFoe):
                blanchon.testAtkEffect(foes[i].get_AtkEffectList()[l])
                fenetre.blit(foes[i].get_AtkEffectList()[l].get_img(), foes[i].get_AtkEffectList()[l].get_rect())

            foes[i].update(blanchon, fps)
            if(foes[i].get_hp() <= 0):
                foes.pop(i)
            else:
                i += 1

        #Affichage Hero
        blanchon.nextImg(fps)
        fenetre.blit(blanchon.get_img(), blanchon.get_rect())
        pygame.draw.rect(fenetre, (0,0,0), (blanchon.get_rect().x, blanchon.get_rect().y - 10, 60, 6))
        pygame.draw.rect(fenetre, (0,255,0), (blanchon.get_rect().x, blanchon.get_rect().y - 10,   int(max(min(blanchon.get_hp() / float(blanchon.get_hpMax()) * 60, 60), 0)),   6))

        pygame.display.flip()
