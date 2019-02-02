import pygame
import niveaux
import time
class Tile:
    ID = 0
    def __init__(self):
        Tile.ID += 1
        self.ID = Tile.ID
        self.x = -100
        self.y = -100
        self.obtenu = False
        self.testgameDisplay = pygame.display.set_mode((600, 600))




    def gamedisplay(self, display_width, display_height):
        return pygame.display.set_mode((display_width, display_height))

    def text_objects(self, text, font):
        white = (255,255,255)
        textsurface = font.render(text, True, white)
        return textsurface, textsurface.get_rect()

    def messagebox(self):
        # genere une boite pour afficher le message
        t.displaytile("images/box.png", 600, 80, 0, 0)

    def message_display(self, text, temps, positionx, positiony):
        # crée un message avec couleur, position et durée d'affichage
        self.messagebox()
        largetext = pygame.font.Font('freesansbold.ttf', 20)
        textsurf, textrect = self.text_objects(text, largetext)
        textrect.center = ((positionx), (positiony))
        self.testgameDisplay.blit(textsurf, textrect)

        pygame.display.update()
        time.sleep(temps)
        self.cleanmessage()

    def cleanmessage(self):
        # nettoie la boite message
        ordo = 0
        i = 0
        while i < 2:
            lst = niveaux.niveau2[i]
            absc = 0
            for y in lst:
                if y == "#":
                    self.testdisplaytile("images/mur1.png", 40, 40, absc, ordo)
                if y == " ":
                    self.testdisplaytile("images/chemin1.png", 40, 40, absc, ordo)
                if y == "D":
                    self.testdisplaytile("images/lava.png", 40, 40, absc, ordo)
                if y == "A":
                    self.testdisplaytile("images/chemin1.png", 40, 40, absc, ordo)
                if y == "G":
                    self.testdisplaytile("images/chemin1.png", 40, 40, absc, ordo)
                if y == "M":
                    self.testdisplaytile("images/chemin1.png", 40, 40, absc, ordo)
                absc += 40
            ordo += 40
            i += 1



    def messagebox(self):
        # genere une boite pour afficher le message
        self.testdisplaytile("images/box.png", 600, 80, 0, 0)

    def cleanscore(self):
        # rafraichi les sprites dans la zone du score
        ordo = 560
        lst = niveaux.niveau2[14]
        absc = 0
        for y in lst:
            if y == "O":
                self.testdisplaytile("images/mur1.png", 40, 40, absc, ordo)
            if y == "X":
                self.testdisplaytile("images/chemin1.png", 40, 40, absc, ordo)
            if y == "D":
                self.testdisplaytile("images/lava.png", 40, 40, absc, ordo)
            if y == "A":
                self.testdisplaytile("images/chemin1.png", 40, 40, absc, ordo)
            if y == "G":
                self.testdisplaytile( "images/chemin1.png", 40, 40, absc, ordo)
            if y == "M":
                self.testdisplaytile( "images/chemin1.png", 40, 40, absc, ordo)
            absc += 40




    def testdisplay(self, img, x, y):
        return self.testgameDisplay.blit(img, (x, y))

    def testdisplaytile(self, img, a, b, x, y):
        sizedImg = pygame.transform.scale(pygame.image.load(img), (a, b))
        return self.testdisplay(sizedImg, x, y)

    def cleantile(self, x, y):
        self.testdisplaytile("images/chemin1.png", 40, 40, x, y)
