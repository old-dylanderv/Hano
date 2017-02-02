# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *

import test
import tuto

import sys

pygame.init()

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
    def __init__(self, screen, items):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.bg = pygame.transform.scale(pygame.image.load("Images/Menu/backgroundcredit.png").convert(), (1280,720))
        self.clock = pygame.time.Clock()
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

class GameMenu(Menu):
    def __init__(self, screen, items, menu, title, anim):
        Menu.__init__(self, screen, items)
        self.anim = anim
        self.title = title
        self.menu = menu

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
        Menu.__init__(self, screen, items)
        self.name = ""
        self.myfont = pygame.font.SysFont("monospace", 15)

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



if __name__ == "__main__":
    screen = pygame.display.set_mode((1280, 720), 0, 32)

    statesBlanchon = {}
    statesBlanchon["idleRight"] = 500
    statesBlanchon["idleLeft"] = 500
    statesBlanchon["moveLeft"] = 100
    statesBlanchon["moveRight"] = 100
    statesBlanchon["atkLeft"] = 75
    statesBlanchon["atkRight"] = 75
    statesBlanchon["crouchLeft"] = 150
    statesBlanchon["crouchRight"] = 150

    imagesBlanchon = {
                      "idleLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha()))), True, False)
                        ],
                      "idleRight":
                        [
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_1.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_idle_2.png").convert_alpha())))
                        ],
                      "moveLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_0.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_2.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha()))), True, False)
                        ],
                      "moveRight":
                        [
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_0.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_2.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_move_1.png").convert_alpha())))
                        ],
                       "atkLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_2.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_3.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_2.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_3.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_4.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_5.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_2.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_3.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_4.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_5.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_6.png").convert_alpha()))), True, False)
                        ],
                        "atkRight":
                         [
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_1.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_2.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa1_3.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_1.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_2.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_3.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_4.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa2_5.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_1.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_2.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_3.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_4.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_5.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_aa3_6.png").convert_alpha())))
                         ],
                      "crouchRight":
                        [
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_crouch_1.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_crouch_2.png").convert_alpha())))
                        ],
                      "crouchLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_crouch_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Blanchon/b_crouch_2.png").convert_alpha()))), True, False)
                        ]
                     }

    statesNinja = {}
    statesNinja["idleRight"] = 500
    statesNinja["idleLeft"] = 500
    statesNinja["moveLeft"] = 100
    statesNinja["moveRight"] = 100
    statesNinja["atkLeft"] = 75
    statesNinja["atkRight"] = 75

    imagesNinja = {
                      "idleLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_idle_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_idle_2.png").convert_alpha()))), True, False)
                        ],
                      "idleRight":
                        [
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_idle_1.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_idle_2.png").convert_alpha())))
                        ],
                      "moveLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_mv.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_mv.png").convert_alpha()))), True, False)
                        ],
                      "moveRight":
                        [
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_1.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_mv.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_1.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_mv.png").convert_alpha())))
                        ],
                       "atkLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_2.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_3.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_4.png").convert_alpha()))), True, False)
                        ],
                        "atkRight":
                         [
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_1.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_2.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_3.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Ninja/n_aa_4.png").convert_alpha())))
                         ]
                     }

    statesSamurai = {}
    statesSamurai["idleRight"] = 500
    statesSamurai["idleLeft"] = 500
    statesSamurai["moveLeft"] = 100
    statesSamurai["moveRight"] = 100
    statesSamurai["atkLeft"] = 75
    statesSamurai["atkRight"] = 75

    imagesSamurai = {
                      "idleLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_idle_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_idle_2.png").convert_alpha()))), True, False)
                        ],
                      "idleRight":
                        [
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_idle_1.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_idle_2.png").convert_alpha())))
                        ],
                      "moveLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_move_0.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_move_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_move_0.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_move_1.png").convert_alpha()))), True, False)
                        ],
                      "moveRight":
                        [
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_move_0.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_move_1.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_move_0.png").convert_alpha()))),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_move_1.png").convert_alpha())))
                        ],
                       "atkLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_atk_1.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_atk_2.png").convert_alpha()))), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_atk_3.png").convert_alpha()))), True, False),
                        ],
                        "atkRight":
                         [
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_atk_1.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_atk_2.png").convert_alpha()))),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Samurai/s_atk_3.png").convert_alpha()))),
                         ]
                     }

    statesBoss = {}
    statesBoss["idleRight"] = 500
    statesBoss["idleLeft"] = 500
    statesBoss["atk1Left"] = 500
    statesBoss["atk1Right"] = 500
    statesBoss["atk2Left"] = 500
    statesBoss["atk2Right"] = 500
    statesBoss["atk3Left"] = 500
    statesBoss["atk3Right"] = 500

    imagesBoss = {
                      "idleLeft":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_idle_1.png").convert_alpha())), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_idle_2.png").convert_alpha())), True, False)
                        ],
                      "idleRight":
                        [
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_idle_1.png").convert_alpha())),
                         pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_idle_2.png").convert_alpha()))
                        ],
                       "atk1Left":
                        [
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_atkranged1_1.png").convert_alpha())), True, False),
                         pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_atkranged1_2.png").convert_alpha())), True, False),
                        ],
                        "atk1Right":
                         [
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_atkranged1_1.png").convert_alpha())),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_atkranged1_2.png").convert_alpha())),
                         ],
                        "atk2Left":
                         [
                          pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_atkranged2_1.png").convert_alpha())), True, False),
                          pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_atkranged2_2.png").convert_alpha())), True, False),
                         ],
                        "atk2Right":
                         [
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_atkranged2_1.png").convert_alpha())),
                          pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_atkranged2_2.png").convert_alpha())),
                         ],
                         "atk3Left":
                          [
                           pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_atkranged3_1.png").convert_alpha())), True, False),
                           pygame.transform.flip(pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_atkranged3_2.png").convert_alpha())), True, False),
                          ],
                         "atk3Right":
                          [
                           pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_atkranged3_1.png").convert_alpha())),
                           pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("Images/Boss/boss_atkranged3_2.png").convert_alpha())),
                          ]
                     }
    blanchon = AnimItem(imagesBlanchon, statesBlanchon, 500, 384)
    ninja = AnimItem(imagesNinja, statesNinja, 1000, 384)
    samurai = AnimItem(imagesSamurai, statesSamurai, 200, 256)
    boss = AnimItem(imagesBoss, statesBoss, 730, 370)
    anim = [blanchon, ninja, boss, samurai]
    jouer = ["Jouer"]
    title = TitleItem("title", 500, 25)
    input_name = NameMenu(screen, jouer)
    menu = [input_name]
    menu_items = ("Jouer", "HighScores", "Credits", "Quitter")

    pygame.display.set_caption('Menu')

    gm = GameMenu(screen, menu_items, menu, title, anim)
    gm.run()
