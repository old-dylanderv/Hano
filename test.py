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
from class_Samurai import *
from class_Ninja import *
from class_Corbeau import *
from class_Demon import *
import class_Menu
from class_Menu import *

#initialisation de pygame
def main(self, name = "Nom Par Defaut"):
    pygame.init()

    WIDTH = 1280
    HEIGHT = 720
    fenetre  = pygame.display.set_mode((WIDTH,HEIGHT), RESIZABLE)

    fond_e = pygame.transform.scale(pygame.image.load("Images/Background/background.png").convert(), (1280,720))

    blanchonAa1 = pygame.image.load("Images/Spell/aa1.png").convert()
    blanchonAa2 = pygame.image.load("Images/Spell/aa2.png").convert()
    blanchonAa3 = pygame.image.load("Images/Spell/aa3.png").convert()
    blanchonAaMidAir = pygame.image.load("Images/Spell/aaMidAir.png").convert()
    blanchonVector = pygame.image.load("Images/Spell/vector.png").convert()

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
                        ],
                       "DRight":
                        [
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_gameover.png").convert_alpha()),
                         pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_gameover.png").convert_alpha())
                        ],
                       "DLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_gameover.png").convert_alpha()), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_gameover.png").convert_alpha()), True, False)
                        ]}
    blanchon_atkList = [
                        Atk("autoHit1", 0.5, 32, 32, {"idleRight":[pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha()],"idleLeft":[pygame.transform.flip(pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha(),True,False)]}, 5, 5, -1, 0, 0, 0, 225),
                        Atk("autoHit2", 0.7, 32, 32, {"idleRight":[pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha()],"idleLeft":[pygame.transform.flip(pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha(),True,False)]}, 10, 5, -2, 0, 0, 0, 300),
                        Atk("autoHit3", 0.7, 32, 32, {"idleRight":[pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha()],"idleLeft":[pygame.transform.flip(pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha(),True,False)]}, 15, 6, -16, 0, 0, 0, 500),
                        Atk("EOF", 4, 32, 17, {"idleRight":[pygame.image.load("Images/Blanchon/vector.png").convert_alpha()],"idleLeft":[pygame.transform.flip(pygame.image.load("Images/Blanchon/vector.png").convert_alpha(),True,False)]}, 10 , 4, -1, 0, 4, 0, 2000),
                        Atk("airAutoHit", 1, 64, 32, {"idleRight":[pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha()],"idleLeft":[pygame.transform.flip(pygame.image.load("Images/Blanchon/particlehit.png").convert_alpha(),True,False)]}, 10, 5, 5, 0, 0, 0, 300)
                       ]
    blanchon = Hero(200, 200, 64, 64, imagesBlanchon, 0.3, 0.7, 8, 6, WIDTH, 5, blanchon_atkList)
    sol = Platform(0, HEIGHT-70, WIDTH, 10, pygame.image.load("Images/plateformtest.png").convert_alpha(), 0.4)

    #INIT ENNEMIS
    foes = []

    #INIT POLICE
    Mult = pygame.font.Font("Polices/Lady Radical.ttf", 25)
    Mult.set_bold(False)
    MultB = pygame.font.Font("Polices/Lady Radical.ttf", 40)
    MultB.set_bold(False)
    damageFont = pygame.font.Font("Polices/Lady Radical.ttf", 30)
    timerFont = pygame.font.Font("Polices/Lady Radical.ttf", 25)
    timerFont.set_bold(False)
    levelFont = pygame.font.Font("Polices/Lady Radical.ttf", 25)
    levelFont.set_bold(False)
    scoreFont = pygame.font.Font("Polices/Lady Radical.ttf", 25)
    levelFont.set_bold(False)

    #INIT VAR DE JEU
    damageArray = []
    timerDamage = 300
    score = 0
    niveau = 1
    salve = 1

    tempsParSalve = 10.0

    #INIT SYSTEM CLOCK
    clock = pygame.time.Clock()
    fps = 60

    while not blanchon.isDead() :
        salve = 1
        #INIT PLATEFORMES
        platforms = []
        platforms.append(Platform(300+(pygame.time.get_ticks()%400)-200, HEIGHT-180, 100, 10, pygame.image.load("Images/plateform.png").convert_alpha(), 1))
        platforms.append(Platform(350+(pygame.time.get_ticks()%100)-50, HEIGHT-280, 100, 10, pygame.image.load("Images/plateform.png").convert_alpha(), 1))
        while salve < 6 and not blanchon.isDead():
            if(salve < 5):
                #AJOUTER DES MOBS A FOES
                i = 0
                while(i < int(niveau+salve/5)):
                    mobId = (i*pygame.time.get_ticks())%4
                    if(mobId == 0):
                        foes.append(Ninja(500, 500, WIDTH, 1+niveau/10))
                    elif(mobId == 1):
                        foes.append(Samurai(700, 500, WIDTH, 1+niveau/10))
                    elif(mobId == 2):
                        foes.append(Archer(50, 500, WIDTH, 1+niveau/10))
                    elif(mobId == 3):
                        foes.append(Corbeau((50+niveau+salve)%(WIDTH-100)+50, 200, WIDTH, 1+niveau/10))
                    i += 1
            else:
                #AJOUTER UN BOSS A FOES
                foes.append(Demon(500, 350, WIDTH, 1+niveau/10))
            niveauLabel = levelFont.render(str(niveau)+" - "+str(salve), 1, (250,250,250))
            timer = tempsParSalve
            timeSave = pygame.time.get_ticks()
            #BOUCLE DE JEU =========================================================================================
            while(len(foes) > 0 and (timer > 0.0 or salve >= 4) and not blanchon.isDead()):
                #GESTION TIMER-----------------------------------------------------------------
                if(timer <= 0.0):
                    timer = 0
                else:
                    timer = timer - (pygame.time.get_ticks() - timeSave)/1000.0
                    timeSave = pygame.time.get_ticks()

                # render text
                if(salve != 5):
                    timerLabel = timerFont.render("{0:.1f}".format(timer)+" sec", 1, (50,100,200))
                else:
                    timerLabel = timerFont.render("BOSS", 1, (50,100,200))
                scoreLabel = scoreFont.render("Score : "+str(int(score)), 1, (200, 200, 100))

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
                #timer
                fenetre.blit(timerLabel, (490, 660))
                fenetre.blit(niveauLabel, (500, 690))

                #Plateformes
                nbPlatf = len(platforms)
                for i in range (0, nbPlatf):
                    fenetre.blit(platforms[i].get_img(), platforms[i].get_rect())

                #GESTION DU HERO----------------------------------------------------------------
                #Affichage Multiplicateur de dégats
                Multipl = Mult.render(u"Mult : ", 1, (255,255,0))
                combo = blanchon.get_combo()
                if(blanchon.get_combo() < 2):
                    MultiplCombo = MultB.render(str(blanchon.get_combo()), 1, (255, 255, 0))
                elif(blanchon.get_combo() < 3):
                    MultiplCombo = MultB.render(str(blanchon.get_combo()), 1, (0, 0, 255))
                elif(blanchon.get_combo() < 4):
                    MultiplCombo = MultB.render(str(blanchon.get_combo()), 1, (255, 0, 255))
                else:
                    MultiplCombo = MultB.render(str(blanchon.get_combo()), 1, (255, 0, 0))

                fenetre.blit(Multipl, (700, 660))
                fenetre.blit(MultiplCombo, (800, 650))
                #Affichage du score
                fenetre.blit(scoreLabel, (700, 690))

                #CoolDown Attaque de Blanchon
                tailleRect1 = 60
                posRect1 = 715
                colorRect = (125,125,125,128)

                if blanchon.get_onGround() == False:
                    cd = blanchon_atkList[4].get_cd()
                    if(float(cd) > 0):
                        pygame.draw.rect(fenetre, (0,0,0), (95, 655, 60, 60))
                    else:
                        pygame.draw.rect(fenetre, (200,200,50), (95, 655, 60, 60))
                    posRect1 = 715 - (60*float(cd))/float(blanchon_atkList[4].get_maxCd())
                    tailleRect1 = (60*float(cd))/float(blanchon_atkList[4].get_maxCd())
                    fenetre.blit(blanchonAaMidAir, (100,660))
                    CdAH = damageFont.render(cd, 1, (255,0,0))
                elif blanchon.get_autoHitTimer3() > 0:
                    pygame.draw.rect(fenetre, (200,200,50), (95, 655, 60, 60))
                    fenetre.blit(blanchonAa3, (100,660))
                    posRect1 = 715 - (60*float("{0:.1f}".format(blanchon.get_autoHitTimer3()/1000)))/float(3)
                    tailleRect1 = (60*float("{0:.1f}".format(blanchon.get_autoHitTimer3()/1000)))/float(3)
                    CdAH = damageFont.render(str("{0:.1f}".format(blanchon.get_autoHitTimer3()/1000)), 1, (255,0,0))

                elif blanchon.get_autoHitTimer2() > 0:
                    pygame.draw.rect(fenetre, (200,200,50), (95, 655, 60, 60))
                    fenetre.blit(blanchonAa2, (100,660))
                    posRect1 = 715 - (60*float("{0:.1f}".format(blanchon.get_autoHitTimer2()/1000)))/float(3)
                    tailleRect1 = (60*float("{0:.1f}".format(blanchon.get_autoHitTimer2()/1000)))/float(3)
                    CdAH = damageFont.render(str("{0:.1f}".format(blanchon.get_autoHitTimer2()/1000)), 1, (255,0,0))
                else:
                    cd = blanchon_atkList[0].get_cd()
                    if(float(cd) > 0):
                        pygame.draw.rect(fenetre, (0,0,0), (95, 655, 60, 60))
                    else:
                        pygame.draw.rect(fenetre, (200,200,50), (95, 655, 60, 60))

                    fenetre.blit(blanchonAa1, (100,660))
                    posRect1 = 715 - ((60*float(cd))/float(blanchon_atkList[0].get_maxCd()))
                    tailleRect1 = (60*float(cd))/float(blanchon_atkList[0].get_maxCd())
                    CdAH = damageFont.render(cd, 1, (255,0,0))

                CaseAa = pygame.Surface((60,tailleRect1), pygame.SRCALPHA)
                CaseAa.fill(colorRect)
                fenetre.blit(CaseAa, (95,posRect1))
                if(float(cd) > 0):
                    fenetre.blit(CdAH, (110, 670))

                if(float(blanchon_atkList[3].get_cd()) > 0):
                    pygame.draw.rect(fenetre, (0,0,0), (175, 655, 60, 60))
                    pygame.draw.rect(fenetre, (255,255,255), (180, 660, 50, 50))
                else:
                    pygame.draw.rect(fenetre, (200,200,50), (175, 655, 60, 60))
                    pygame.draw.rect(fenetre, (255,255,255), (180, 660, 50, 50))

                fenetre.blit(blanchonVector, (189,677))
                tailleRect2 = 65
                posRect2 = 715

                posRect2 = 715 - (60*float(blanchon_atkList[3].get_cd()))/float(blanchon_atkList[3].get_maxCd())
                tailleRect2 = (60*float(blanchon_atkList[3].get_cd()))/float(blanchon_atkList[3].get_maxCd())
                CaseAa = pygame.Surface((60,tailleRect2), pygame.SRCALPHA)
                CaseAa.fill((125,125,125,128))
                fenetre.blit(CaseAa, (175,posRect2))

                CdProj = damageFont.render(str(blanchon_atkList[3].get_cd()), 1, (255,0,0))
                if(float(blanchon_atkList[3].get_cd()) > 0):
                    fenetre.blit(CdProj, (190, 670))
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

                #AFFICHAGE DES DEGATS----------------------------------------------------------
                i = 0
                while i < len(damageArray):
                    if(damageArray[i][2] > 0):
                        fenetre.blit(damageArray[i][0], damageArray[i][1])
                        damageArray[i][2] = damageArray[i][2] - (1000/fps)
                        i += 1
                    else:
                        damageArray.pop(i)

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
                        hpBefore = foes[i].get_hp()
                        foes[i].testAtkEffect(blanchon.get_AtkEffectList()[k])
                        degats = foes[i].get_hp() - hpBefore
                        if (degats < 0.0):
                            damageArray.append([damageFont.render(str(degats), 1, (50,150,255)),(foes[i].get_x(), foes[i].get_y()-40), timerDamage])


                    nbAtkFoe = len(foes[i].get_AtkEffectList())
                    for l in range (0, nbAtkFoe):
                        hpBefore = blanchon.get_hp()
                        blanchon.testAtkEffect(foes[i].get_AtkEffectList()[l])
                        degats = blanchon.get_hp() - hpBefore
                        if (degats < 0):
                            damageArray.append([damageFont.render(str(degats), 1, (255,0,0)), (blanchon.get_x(), blanchon.get_y()-40), timerDamage])

                        fenetre.blit(foes[i].get_AtkEffectList()[l].get_img(), foes[i].get_AtkEffectList()[l].get_rect())

                    foes[i].update(blanchon, fps)
                    if(foes[i].get_hp() <= 0):
                        #AJOUT DES POINTS AU SCORE
                        score += foes[i].get_hpMax()*foes[i].get_hpMax()
                        foes.pop(i)
                    else:
                        i += 1

                for i in range (0, nbAtkHero):
                    fenetre.blit(blanchon.get_AtkEffectList()[k].get_img(), blanchon.get_AtkEffectList()[k].get_rect())

                #Affichage Hero
                blanchon.nextImg(fps)
                fenetre.blit(blanchon.get_img(), blanchon.get_rect())
                pygame.draw.rect(fenetre, (0,0,0), (blanchon.get_rect().x, blanchon.get_rect().y - 10, 60, 6))
                pygame.draw.rect(fenetre, (0,255,0), (blanchon.get_rect().x, blanchon.get_rect().y - 10,   int(max(min(blanchon.get_hp() / float(blanchon.get_hpMax()) * 60, 60), 0)),   6))

                pygame.display.flip()
            #AJOUTE DES POINTS AU SCORE
            score += (tempsParSalve - timer)*500
            salve += 1
        niveau += 1

    keyR = False
#    while(keyR == False):
#        for event in pygame.event.get():
#            if event.type == QUIT: 	#si l'utilisateur clique sur la croix
#                sys.exit()          #on ferme la fenêtre
#            if event.type == KEYDOWN:
#                keyR = True

    dieMenu = class_Menu.DieMenu(fenetre, ("Rejouer", "RetourMenu"), self.name)
    dieMenu.run()

#        fontGO = pygame.font.SysFont("monospace", 40)
#        labelGO = fontGO.render("GAME OVER", 1, (150,50,50))
#        fenetre.blit(labelGO, (300, 300))
    pygame.display.flip()

    #RENVOYER AU MENU
