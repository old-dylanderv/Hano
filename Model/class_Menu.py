# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *

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
        self.anim = anim
        self.title = title
        self.menu = menu
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
                    self.menu[0].run()
                if self.cur_item == 1:
                    tuto.main(self)
                if self.cur_item == 2:
                    self.menu[1].run()

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
        self.myfont = pygame.font.SysFont("monospace", 15)
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

    def input_name(self, key):
        if key == K_RETURN:
            test.main(self, self.name)
        elif (key >= 65 and key <= 90) or (key >= 97 and key <= 122) or (key == 32):
            self.name = self.name + str(unichr(key))
        elif key == 8:
            self.name = self.name[:len(self.name)-1]


    def run(self):
        while 1:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.input_name(event.key)

            self.screen.blit(self.bg, (0,0))

            name = self.myfont.render("Entrez votre nom : "+self.name, 1, (255,255,0))
            self.screen.blit(name, (0,0))

            pygame.display.flip()


class DieMenu(Menu):
    def __init__(self, screen, items, name, score):
        Menu.__init__(self, screen)
        self.font = scoreFont = pygame.font.Font("Polices/Lady Radical.ttf", 25)
        self.score = score
        self.name = name
        self.items = []
        for index, item in enumerate(items):
            menu_item = SelectItem(item)

            t_h = len(items) * menu_item.height
            pos_x = 515
            pos_y = 150 + (menu_item.height * (index * 1.2)) + menu_item.height

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
                    test.main(self, self.name)
                if self.cur_item == 1:
                    monMenu.main()

    def run(self):
        while 1:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.set_item_selection(event.key)



            pygame.draw.rect(self.screen, (127,127,127), (390, 95, 500, 320))
            self.screen.blit(pygame.image.load("Images/Menu/GameOver.png").convert_alpha(), (460,95))
            label = self.font.render(self.name+" - Score : "+str(int(self.score)), 1, (200, 200, 100))
            self.screen.blit(label, (390,95))
            for item in self.items:
                self.screen.blit(item.get_image(), item.position)

            pygame.display.flip()

class CreditMenu(Menu):
    def __init__(self, screen):
        Menu.__init__(self, screen)
        self.bg = pygame.transform.scale(pygame.image.load("Images/Menu/backgroundcredit.png").convert(), (1280,720))
        self.myfont = pygame.font.Font("Polices/Lady Radical.ttf", 25)

    def input_name(self, key):
        if key == K_RETURN:
            monMenu.main()


    def run(self):
        while 1:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.input_name(event.key)

            self.screen.blit(self.bg, (0,0))

            name = self.myfont.render("Entrez votre nom : ", 1, (255,255,0))
            self.screen.blit(name, (0,0))

            name = self.myfont.render("Entrez votre nom : ", 1, (255,255,0))
            self.screen.blit(name, (1000,0))

            pygame.display.flip()
