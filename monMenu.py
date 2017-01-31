# -*- coding:Utf-8 -*-
import pygame

pygame.init()

class MenuItem():
    def __init__(self, pos_x = 0, pos_y = 0):
        self.image = pygame.image.load("Images/Menu/"+".png")
        self.image = pygame.image.load("Images/Blanchon/b_idle_1.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
        self.is_selected = False

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

class GameMenu():
    def __init__(self, screen, items, bg_color=(127,127,127)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item)

            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index*2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

        self.cur_item = 1

    def set_item_selection(self, key):


        if key == pygame.K_UP and self.cur_item > 0:
            self.cur_item -= 1
        elif key == pygame.K_UP and self.cur_item == 0:
            self.cur_item = len(self.items) - 1
        elif key == pygame.K_DOWN and self.cur_item < len(self.items) - 1:
            self.cur_item += 1
        elif key == pygame.K_DOWN and self.cur_item == len(self.items) - 1:
            self.cur_item = 0


    def run(self):
        while 1:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.set_item_selection(event.key)


            self.screen.fill(self.bg_color)

            for item in self.items:
                self.screen.blit(item.image, item.position)

            pygame.display.flip()


if __name__ == "__main__":
    screen = pygame.display.set_mode((640, 480), 0, 32)

    menu_items = ("Jouer", "Option", "Crédits", "Quitter")

    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen, menu_items)
    gm.run()
