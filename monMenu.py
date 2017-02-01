# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *

import test

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
        print(pygame.time.get_ticks() % len(self.states))
        state = self.states.keys()[(pygame.time.get_ticks() % len(self.states))]
        self.changeState(state)

    def get_image(self):
        return self.images.get(self.state)[self.indexImg]

class GameMenu():
    def __init__(self, screen, items, title, hero):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.bg = pygame.transform.scale(pygame.image.load("Images/Menu/backgroundcredit.png").convert(), (1280,720))
        self.clock = pygame.time.Clock()
        self.hero = hero
        self.title = title

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
                    test.main(self)


    def run(self):
        while 1:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.set_item_selection(event.key)


            self.hero.nextImg(60)
            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.title.get_image(), self.title.get_position())
            self.screen.blit(self.hero.get_image(), self.hero.get_position())

            for item in self.items:
                self.screen.blit(item.get_image(), item.position)

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
    statesBlanchon["crouchLeft"] = 75
    statesBlanchon["crouchRight"] = 75

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

    menu_items = ("Jouer", "HighScores", "Credits", "Quitter")
    title = TitleItem("title", 500, 25)
    blanchon = AnimItem(imagesBlanchon, statesBlanchon, 500, 384)
    pygame.display.set_caption('Menu')
    gm = GameMenu(screen, menu_items, title, blanchon)
    gm.run()
