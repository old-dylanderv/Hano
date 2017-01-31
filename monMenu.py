# -*- coding:Utf-8 -*-
import pygame

pygame.init()

class MenuItem():
    def __init__(self, img, pos_x = 0, pos_y = 0):
        self.imageNS = pygame.image.load("Images/Menu/"+img+"NS.png").convert_alpha()
        self.imageS = pygame.image.load("Images/Menu/"+img+"S.png").convert_alpha()
        self.width = self.imageNS.get_rect().width
        self.height = self.imageNS.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
        self.is_selected = False

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_selected(self, selected):
        self.is_selected = selected

    def get_image(self):
        if self.is_selected:
            return self.imageS
        else:
            return self.imageNS

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

        self.cur_item = 0
        self.items[self.cur_item].set_selected(True)

    def set_item_selection(self, key):
        if self.cur_item is None:
            self.cur_item = 0
        else:
            print(self.cur_item)
            # Find the chosen item
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
                self.screen.blit(item.get_image(), item.position)

            pygame.display.flip()


if __name__ == "__main__":
    screen = pygame.display.set_mode((1280, 720), 0, 32)

    menu_items = ("Jouer", "Credits")

    pygame.display.set_caption('Menu')
    gm = GameMenu(screen, menu_items)
    gm.run()
