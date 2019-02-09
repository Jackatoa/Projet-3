import pygame
import time


class Tile:
    """Contain all the functions relative to all tiles"""
    gamedisplay = pygame.display.set_mode((600, 600))

    def __init__(self, img=None, text=None):
        self.x = -100
        self.y = -100
        self.img = img
        self.displayed = True
        self.text = text

    def set_pos(self, x, y):
        """Set positions"""
        self.x = x
        self.y = y

    def get_pos(self):
        """Return positions"""
        return self.x, self.y

    def get_sized(self, height, lenght, img=None):
        """Change the size of an image"""
        if img is None:
            img = self.img
        sizedimg = pygame.transform.scale(pygame.image.load(img), (height, lenght))
        return sizedimg

    def display(self, height=40, lenght=40):
        """Display a tile"""
        Tile.gamedisplay.blit(self.get_sized(height, lenght), (self.x, self.y))

    def should_it_be_displayed(self):
        """Check if a tile should be displayed"""
        if self.displayed:
            return self.display()

    def clean_a_tile(self, img=None):
        """Clean the tile, take the new tile as parameter"""
        if img is None:
            img = "images/way.png"
        Tile.gamedisplay.blit(self.get_sized(40, 40, img), (self.x, self.y))

    def clean_ui(self):
        """Clean all the UI line"""
        way = Tile("images/way.png")
        wall = Tile("images/wall.png")
        maplist = [line.rstrip('\n') for line in open('levels.txt')]
        ordo = 0
        for x in maplist:
            absc = 0
            for y in list(x):
                if y == "M" or y == "G" or y == " " or y == "A":
                    way.set_pos(absc, ordo)
                    way.display()
                elif y == "#":
                    wall.set_pos(absc, ordo)
                    wall.display()
                absc += 40
            ordo += 40

    def display_message_box(self):
        """A nice box to fit message in"""
        box = Tile("images/box.png")
        box.set_pos(0, 0)
        box.display(600, 80)

    def text_objects(self, text, font):
        """Generate the texts"""
        white = (255, 255, 255)
        textsurface = font.render(text, True, white)
        return textsurface, textsurface.get_rect()

    def message_display_text(self, temps, text=None):
        """Display the texts"""
        t = Tile()
        t.display_message_box()
        if text is None:
            text = self.text
        largetext = pygame.font.Font('freesansbold.ttf', 20)
        textsurf, textrect = self.text_objects(text, largetext)
        textrect.center = (300, 40)
        Tile.gamedisplay.blit(textsurf, textrect)
        pygame.display.update()
        time.sleep(temps)
        t.clean_message()

    def clean_message(self):
        """Clean the texts"""
        way = Tile("images/way.png")
        wall = Tile("images/wall.png")
        lava = Tile("images/lava.png")
        maplist = [line.rstrip('\n') for line in open('levels.txt')]
        ordo = 0
        i = 0
        while i < 2:
            absc = 0
            for y in maplist[i]:
                if y == "#":
                    wall.set_pos(absc, ordo)
                    wall.display()
                elif y == "D":
                    lava.set_pos(absc, ordo)
                    lava.display()
                elif y == " " or "A" or "G" or "M":
                    way.set_pos(absc, ordo)
                    way.display()
                absc += 40
            ordo += 40
            i += 1
