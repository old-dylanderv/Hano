# -*- coding:Utf-8 -*-
import sys
sys.path.append('Model/')
import pygame
from pygame.locals import *
from class_Menu import *

import test
import tuto

import sys




def main():
    pygame.init()

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


    blanchon = AnimItem(imagesBlanchon, statesBlanchon, 500, 384)
    anim = [blanchon]
    jouer = ["Jouer"]
    title = TitleItem("title", 500, 25)
    input_name = NameMenu(screen, jouer)
    credit_menu = CreditMenu(screen)
    leaderboard_menu = LeaderboardMenu(screen)
    menu = [input_name, credit_menu, leaderboard_menu]

    menu_items = ("DifNorm", "DifHard", "Tutoriel", "HighScores", "Credits", "Quitter")

    pygame.display.set_caption('Menu')

    gm = GameMenu(screen, menu_items, menu, title, anim)
    gm.run()
