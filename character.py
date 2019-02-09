from tile import Tile

import pygame


class Character(Tile):
    """Contain the functions relative to the main character"""
    def __init__(self, img, text):
        Tile.__init__(self, img, text)
        self.startx = -100
        self.starty = -100

    def set_starting_pos(self, x, y):
        """Set the initial position"""
        self.startx = x
        self.starty = y
        self.set_pos(x, y)

    def get_starting_pos(self):
        """Return the initial position"""
        return self.startx, self.starty

    def go_to_start(self):
        """Set the main character position to the initial one"""
        self.set_pos(*self.get_starting_pos())

    def check_move(self, x, y):
        """Check if the move is possible"""
        ordo = 0
        maplist = [line.rstrip('\n') for line in open('levels.txt')]
        walllst = []
        for a in maplist:
            absc = 0
            for b in list(a):
                if b == "#":
                    walllst.append((absc, ordo))
                absc += 40
            ordo += 40
        if (x, y) not in walllst:
            return True

    def key_input_check(self, addx, addy):
        """Modifie position if move is possible"""
        if self.check_move(self.x + addx, self.y + addy):
            self.clean_a_tile()
            self.set_pos(self.x + addx, self.y + addy)

    def key_input(self, event):
        """Check key pressed to move"""
        if event.key == pygame.K_LEFT:
            self.key_input_check(-40, 0)
        if event.key == pygame.K_RIGHT:
            self.key_input_check(40, 0)
        if event.key == pygame.K_UP:
            self.key_input_check(0, -40)
        if event.key == pygame.K_DOWN:
            self.key_input_check(0, 40)

    def is_jack_on_item(self, item):
        """Check if the main character is on the same position as an item"""
        if self.get_pos() == item.get_pos() and item.collected is not True:
            return item.item_event()
