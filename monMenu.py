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
