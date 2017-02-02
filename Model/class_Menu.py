# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *

import leaderboard
from leaderboard import *
import monMenu
import test
import tuto

import sys

class MenuItem():
    def __init__(self, pos_x = 0, pos_y = 0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def get_position(self):
        return self.position

class SelectItem(MenuItem):
    def __init__(self, img, pos_x = 0, pos_y = 0):
        MenuItem.__init__(self, pos_x, pos_y)
        self.imageNS = pygame.image.load("Images/Menu/"+img+"NS.png").convert_alpha()
        self.imageS = pygame.image.load("Images/Menu/"+img+"S.png").convert_alpha()
        self.width = self.imageNS.get_rect().width
        self.height = self.imageNS.get_rect().height
        self.dimensions = (self.width, self.height)
        self.is_selected = False

    def set_selected(self, selected):
        self.is_selected = selected

    def get_image(self):
        if self.is_selected:
            return self.imageS
        else:
            return self.imageNS

class TitleItem(MenuItem):
    def __init__(self, img, pos_x = 0, pos_y = 0):
        MenuItem.__init__(self, pos_x, pos_y)
        self.image = pygame.image.load("Images/Menu/"+img+".png").convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.dimensions = (self.width, self.height)

    def get_image(self):
        return self.image

class AnimItem(MenuItem):
    def __init__(self, img, states, pos_x = 0, pos_y = 0):
        MenuItem.__init__(self, pos_x, pos_y)
        self.images = img
        self.indexImg = 0
        self.states = states
        self.state = self.states.keys()[0]
        self.timerAnim = 0

    def changeState(self, newState):
        if(newState != self.state):
            oldState = self.state
            try:
                self.indexImg = 0
                self.timerAnim = 0
                self.state = self.states.keys()[self.states.keys().index(newState)]
            except ValueError:
                self.state = oldState
        else:
            self.indexImg = 0
            self.timerAnim = 0

    def nextImg(self, fps):
        self.timerAnim = self.timerAnim + (1000/fps)
        timeState = self.states.get(self.state)
        if self.timerAnim > timeState:
            self.timerAnim = self.timerAnim - timeState
            self.indexImg = self.indexImg + 1
            if(self.indexImg == len(self.images.get(self.state))):
                self.randState()
            self.timerAnim = 0

    def randState(self):
        state = self.states.keys()[(pygame.time.get_ticks() % len(self.states))]
        self.changeState(state)

    def get_image(self):
        return self.images.get(self.state)[self.indexImg]

class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.clock = pygame.time.Clock()

class GameMenu(Menu):
    def __init__(self, screen, items, menu, title, anim):
        Menu.__init__(self, screen)
        self.bg = pygame.transform.scale(pygame.image.load("Images/Menu/backgroundcredit.png").convert(), (1280,720))
        self.jouer = pygame.image.load("Images/Menu/JouerNS.png").convert_alpha()
        self.anim = anim
        self.title = title
        self.menu = menu
        self.items = []
        for index, item in enumerate(items):
            menu_item = SelectItem(item)
            if(index == 0):
                pos_x = 30
                pos_y = 130 + (menu_item.height * (index * 1.2)) + menu_item.height
            elif(index == 1):
                pos_x = 180
                pos_y = 180
            else:
                pos_x = 50
                pos_y = (menu_item.height * (index * 1.2)) + menu_item.height

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)
        self.cur_item = 0
        self.items[self.cur_item].set_selected(True)

    def set_item_selection(self, key):
        if self.cur_item is None:
            self.cur_item = 0
        else:
            if key == pygame.K_UP and self.cur_item > 0:
                self.items[self.cur_item].set_selected(False)
                self.cur_item -= 1
                self.items[self.cur_item].set_selected(True)
            elif key == pygame.K_UP and self.cur_item == 0:
                self.items[self.cur_item].set_selected(False)
                self.cur_item = len(self.items) - 1
                self.items[self.cur_item].set_selected(True)
            elif key == pygame.K_DOWN and self.cur_item < len(self.items) - 1:
                self.items[self.cur_item].set_selected(False)
                self.cur_item += 1
                self.items[self.cur_item].set_selected(True)
            elif key == pygame.K_DOWN and self.cur_item == len(self.items) - 1:
                self.items[self.cur_item].set_selected(False)
                self.cur_item = 0
                self.items[self.cur_item].set_selected(True)
            elif key == K_RETURN:
                if self.cur_item == 0:
                    self.menu[0].run(False)
                if self.cur_item == 1:
                    self.menu[0].run(True)
                if self.cur_item == 2:
                    tuto.main(self)
                if self.cur_item == 3:
                    self.menu[2].run(readFile(False), readFile(True),)
                if self.cur_item == 4:
                    self.menu[1].run()
                if self.cur_item == 5:
                    sys.exit()

    def run(self):
        while 1:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.set_item_selection(event.key)


            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.title.get_image(), self.title.get_position())
            self.screen.blit(self.jouer, (50,70))

            for perso in self.anim:
                perso.nextImg(60)
                self.screen.blit(perso.get_image(), perso.get_position())

            for item in self.items:
                self.screen.blit(item.get_image(), item.position)

            pygame.display.flip()

class NameMenu(Menu):
    def __init__(self, screen, items):
        Menu.__init__(self, screen)
        self.bg = pygame.transform.scale(pygame.image.load("Images/Menu/backgroundcredit.png").convert(), (1280,720))
        self.name = ""
        self.myfont = pygame.font.Font("Polices/Lady Radical.ttf", 42)
        self.items = []
        for index, item in enumerate(items):
            menu_item = SelectItem(item)

            t_h = len(items) * menu_item.height
            pos_x = 50
            pos_y = 75 + (menu_item.height * (index * 1.2)) + menu_item.height

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)
        self.cur_item = 0
        self.items[self.cur_item].set_selected(True)

    def input_name(self, key, difHard):
        if key == K_RETURN:
            test.main(self, self.name, difHard)
        elif (key >= 65 and key <= 90) or (key >= 97 and key <= 122) or (key == 32):
            self.name = self.name + str(unichr(key))
        elif key == 8:
            self.name = self.name[:len(self.name)-1]


    def run(self, difHard):
        while 1:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.input_name(event.key, difHard)

            self.screen.blit(self.bg, (0,0))

            name = self.myfont.render("Entrez votre nom : ", 1, (255,255,0))

            self.screen.blit(name, ((self.scr_width/2)-170,(self.scr_height/2)-150))

            textarea = self.myfont.render(self.name,1,(0,0,0))

            self.screen.blit(textarea,((self.scr_width/2)-9*len(self.name),self.scr_height/2-50))



            pygame.display.flip()


class DieMenu(Menu):
    def __init__(self, screen, items, name, score):
        Menu.__init__(self, screen)
        self.font = pygame.font.Font("Polices/Lady Radical.ttf", 25)
        self.img = pygame.transform.scale(pygame.image.load("Images/Menu/Panneau.png").convert_alpha(), (550, 450))
        self.score = score
        self.name = name
        self.items = []
        for index, item in enumerate(items):
            menu_item = SelectItem(item)

            t_h = len(items) * menu_item.height
            pos_x = 530
            pos_y = 200 + (menu_item.height * (index * 1.2)) + menu_item.height

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)
        self.cur_item = 0
        self.items[self.cur_item].set_selected(True)


    def set_item_selection(self, key, difHard):
        if self.cur_item is None:
            self.cur_item = 0
        else:
            if key == pygame.K_UP and self.cur_item > 0:
                self.items[self.cur_item].set_selected(False)
                self.cur_item -= 1
                self.items[self.cur_item].set_selected(True)
            elif key == pygame.K_UP and self.cur_item == 0:
                self.items[self.cur_item].set_selected(False)
                self.cur_item = len(self.items) - 1
                self.items[self.cur_item].set_selected(True)
            elif key == pygame.K_DOWN and self.cur_item < len(self.items) - 1:
                self.items[self.cur_item].set_selected(False)
                self.cur_item += 1
                self.items[self.cur_item].set_selected(True)
            elif key == pygame.K_DOWN and self.cur_item == len(self.items) - 1:
                self.items[self.cur_item].set_selected(False)
                self.cur_item = 0
                self.items[self.cur_item].set_selected(True)
            elif key == K_RETURN:
                if self.cur_item == 0:
                    test.main(self, self.name, difHard)
                if self.cur_item == 1:
                    monMenu.main()

    def run(self, difHard):
        writeFile(addScore(readFile(difHard), self.score, self.name), difHard)
        while 1:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.set_item_selection(event.key, difHard)



            self.screen.blit(self.img, (390, 80))
            self.screen.blit(pygame.image.load("Images/Menu/GameOver.png").convert_alpha(), (480,140))
            label = self.font.render(self.name+" - Score : "+str(int(self.score)), 1, (250, 250, 150))
            self.screen.blit(label, (480,240))
            for item in self.items:
                self.screen.blit(item.get_image(), item.position)

            pygame.display.flip()

class CreditMenu(Menu):
    def __init__(self, screen):
        Menu.__init__(self, screen)
        self.bg = pygame.transform.scale(pygame.image.load("Images/Menu/backgroundcredit.png").convert(), (1280,720))
        self.myfont = pygame.font.Font("Polices/Lady Radical.ttf", 25)
        self.myfontMini = pygame.font.Font("Polices/Lady Radical.ttf", 15)

    def input_name(self, key):
        if key == K_RETURN:
            monMenu.main()


    def run(self):
        idle = [
                pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Medite/b_mediteidle_1.png").convert_alpha())),
                pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Medite/b_mediteidle_2.png").convert_alpha()))
                ]
        rect = pygame.Rect(565, 290, 128, 128)
        idle1 = True
        timeAnim = 700
        timeStart = pygame.time.get_ticks()
        while 1:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.input_name(event.key)

            self.screen.blit(self.bg, (0,0))

            #Affichage blanchon meditation
            if(idle1 == True):
                self.screen.blit(idle[0], rect)
            else:
                self.screen.blit(idle[1], rect)

            #Alternance des animations
            timeAnim = timeAnim - (pygame.time.get_ticks() - timeStart)
            timeStart = pygame.time.get_ticks()
            if(timeAnim <= 0.0):
                timeAnim = 700
                idle1 = not idle1

            #Partie texte pour les remerciements
            graphiste = self.myfont.render("Avec l'aide de : ", 1, (0,0,0))
            self.screen.blit(graphiste, (260,500))
            dumas = self.myfont.render("    - Stack-Overflow", 1, (0,0,0))
            self.screen.blit(dumas, (260,530))
            sorin = self.myfont.render("    - Pygame.org ", 1, (0,0,0))
            self.screen.blit(sorin, (260,560))

            #Partie texte pour les concepteurs
            graphiste = self.myfont.render("Concepteurs : ", 1, (0,0,0))
            self.screen.blit(graphiste, (190,300))
            dumas = self.myfont.render("    - ORTHLIEB  Teo", 1, (0,0,0))
            self.screen.blit(dumas, (190,330))
            sorin = self.myfont.render("    - DERVAUX  Dylan ", 1, (0,0,0))
            self.screen.blit(sorin, (190,360))

            #Partie texte pour les devs
            graphiste = self.myfont.render("Developpeurs : ", 1, (0,0,0))
            self.screen.blit(graphiste, (520,150))
            dumas = self.myfont.render("    - ORTHLIEB  Teo", 1, (0,0,0))
            self.screen.blit(dumas, (520,180))
            sorin = self.myfont.render("    - DERVAUX  Dylan ", 1, (0,0,0))
            self.screen.blit(sorin, (520,210))

            #Partie texte pour les graphistes
            graphiste = self.myfont.render("Graphistes : ", 1, (0,0,0))
            self.screen.blit(graphiste, (800,300))
            dumas = self.myfont.render("    - DUMAS  Remi", 1, (0,0,0))
            self.screen.blit(dumas, (800,330))
            sorin = self.myfont.render("    - SORIN-DOIZE  Clement ", 1, (0,0,0))
            self.screen.blit(sorin, (800,360))
            gineys = self.myfont.render("   - GINEYS  Julien", 1, (0,0,0))
            self.screen.blit(gineys, (800,390))

            #Partie texte pour ^^
            graphiste = self.myfont.render("Inspire d'une histoire (presque) vraie ", 1, (0,0,0))
            self.screen.blit(graphiste, (780,530))

            #Partie texte pour quitter
            quit = self.myfontMini.render("Appuyer sur 'Entree' pour ", 1, (0,0,0))
            self.screen.blit(quit, (1100,600))
            quit2 = self.myfontMini.render("retourner au menu principal ", 1, (0,0,0))
            self.screen.blit(quit2, (1100,620))



            pygame.display.flip()

class LeaderboardMenu(Menu):
    def __init__(self, screen):
        Menu.__init__(self, screen)
        self.bg = pygame.transform.scale(pygame.image.load("Images/Menu/backgroundcredit.png").convert(), (1280,720))
        self.img = pygame.image.load("Images/Menu/HighScoresNS.png").convert_alpha()
        self.myfont = pygame.font.Font("Polices/Lady Radical.ttf", 25)
        self.myfontBig = pygame.font.Font("Polices/Lady Radical.ttf", 35)
        self.myfontMini = pygame.font.Font("Polices/Lady Radical.ttf", 15)

    def input_name(self, key):
        if key == K_RETURN:
            monMenu.main()


    def run(self, tabScoreMoyen, tabScoreHard):
        while 1:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.input_name(event.key)

            self.screen.blit(self.bg, (0,0))

            self.screen.blit(self.img, (520,100))

            normal = self.myfontBig.render("Normal", 1, (0,0,0))
            self.screen.blit(normal, (190,190))
            i = 0
            while i < len(tabScoreMoyen):
                score = self.myfont.render(tabScoreMoyen[i][0]+" - "+tabScoreMoyen[i][1], 1, (0,0,0))
                self.screen.blit(score, (190,250 + (30 * i)))
                i += 1

            insane = self.myfontBig.render("Insane", 1, (0,0,0))
            self.screen.blit(insane, (900,190))
            i = 0
            while i < len(tabScoreHard):
                score = self.myfont.render(tabScoreHard[i][0]+" - "+tabScoreHard[i][1], 1, (0,0,0))
                self.screen.blit(score, (900,250 + (30 * i)))
                i += 1

            #Partie texte pour quitter
            quit = self.myfontMini.render("Appuyer sur 'Entree' pour ", 1, (0,0,0))
            self.screen.blit(quit, (1100,600))
            quit2 = self.myfontMini.render("retourner au menu principal ", 1, (0,0,0))
            self.screen.blit(quit2, (1100,620))



            pygame.display.flip()
