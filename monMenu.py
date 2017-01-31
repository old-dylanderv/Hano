# -*- coding:Utf-8 -*-
import pygame

pygame.init()

class Item():
    def __init__(self, color, text, width = 0, height = 0, (x, y) = (0, 0)):
        self.color = color
        self.text = text
        self.rect = (x, y, width, height)
        self.position = x, y

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_color(self, color):
        self.color = color

    def get_position(self):
        return self.position


class Menu():
    def __init__(self, window, items, color):
        self.window = window
        self.width = window.get_rect().width
        self.height = window.get_rect().height
        self.color = color
        self.items = items
        self.selectedItem = 0
        self.items = []
        for index, item in enumerate(items):
            items = Item((255,255,255), item)

            t_h = len(items) * items.height
            pos_x = (self.width / 2) - (items.width / 2)

            pos_y = (self.height / 2) - (t_h / 2) + ((index*2) + index * items.height)

            items.set_position(pos_x, pos_y)
            self.items.append(items)

    def set_select_item(self, key):
        for item in self.items:
            item.set_color((255,255,255))

        if key == pygame.K_UP and self.selectedItem > 0:
            self.selectedItem -= 1
        elif key == pygame.K_UP and self.selectedItem == 0:
            self.selectedItem = len(self.items) - 1
        elif key == pygame.K_DOWN and self.selectedItem < len(self.items) - 1:
            self.selectedItem += 1
        elif key == pygame.K_DOWN and self.selectedItem == len(self.items) - 1:
            self.selectedItem = 0

        self.items[self.selectedItem].set_font_color(RED)

    def run(self):
        while 1:
            #self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.set_item_selection(event.key)

            self.window.fill(self.color)

            for item in self.items:
                self.window.blit(item.text, item.position)

            pygame.display.flip()

if __name__ == "__main__":
    window = pygame.display.set_mode((1280, 720), 0, 32)
    items = ('Jouer', 'Jouéje', 'Joueraje')
    gm = Menu(window, items, (0,0,0))
    gm.run()
