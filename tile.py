import pygame
import levels
import time
import random


class Tile:
    """Contain all the tiles functions"""
    level = []
    gamecontinue = True
    itemscollected = 0
    ID = 0
    gamedisplay = pygame.display.set_mode((600, 600))
    invstart = 85

    def __init__(self, img=None, text=None, height=40, lenght=40, displayed=True, x=-100, y=-100,
                 invx=-100, invy=-100):
        Tile.ID += 1
        self.ID = Tile.ID
        self.startx = x
        self.starty = y
        self.x = x
        self.y = y
        self.img = img
        self.height = height
        self.lenght = lenght
        self.displayed = displayed
        self.obtenu = False
        self.invx = invx
        self.invy = invy
        self.text = text

    def setpos(self, x, y):
        """Set positions"""
        self.x = x
        self.y = y

    def getpos(self):
        """Return positions"""
        return self.x, self.y

    def getdisplayed(self, trueorfalse):
        """Set the displayed attribute"""
        self.displayed = trueorfalse

    def getsized(self, img=None):
        """Change the size of an image"""
        if img is None:
            img = self.img
        sizedimg = pygame.transform.scale(pygame.image.load(img), (self.height, self.lenght))
        return sizedimg

    def display(self):
        """Display a tile"""
        Tile.gamedisplay.blit(self.getsized(), (self.x, self.y))

    def cleanatile(self, img):
        """Clean the tile, take the new tile as parameter"""
        Tile.gamedisplay.blit(self.getsized(img), (self.x, self.y))

    def keyinput(self, event):
        """Check key pressed to move"""
        if event.key == pygame.K_LEFT:
            self.keyinputcheck(-40, 0)
        if event.key == pygame.K_RIGHT:
            self.keyinputcheck(40, 0)
        if event.key == pygame.K_UP:
            self.keyinputcheck(0, -40)
        if event.key == pygame.K_DOWN:
            self.keyinputcheck(0, 40)

    def keyinputcheck(self, addx, addy):
        """Modifie position if move is possible"""
        if self.checkmove(self.x + addx, self.y + addy):
            self.cleanatile("images/way.png")
            self.setpos(self.x + addx, self.y + addy)

    def checkmove(self, x, y):
        """Check if the move is possible"""
        ordo = 0
        walllst = []
        for a in Tile.level:
            absc = 0
            for b in list(a):
                if b == "#":
                    walllst.append((absc, ordo))
                absc += 40
            ordo += 40
        if (x, y) not in walllst:
            return True

    def shoulditbedisplayed(self):
        """Check if an image should be displayed"""
        if self.displayed:
            self.display()

    def checkpos(self, item):
        """Compare the position between the char and an item"""
        if (self.x, self.y) == (item.x, item.y):
            return True

    def checkpositems(self, item, temps):
        """Change the state of an item"""
        if self.checkpos(item) and item.obtenu is not True:
            item.message_display(temps)
            Tile.itemscollected += 1
            item.obtenu = True
            item.displayed = False
            item.inventorypos()

    def checkitems(self, a, b, c):
        """Check if the character have picked up all items"""
        if a.obtenu is not True or b.obtenu is not True or c.obtenu is not True:
            return True

    def checkposevent(self, a, b, c, d, e, f):
        """contain all the positions checks"""
        t = Tile()
        self.checkpositems(a, 1)
        self.checkpositems(b, 1)
        self.checkpositems(c, 1)
        if self.checkpos(d):
            self.message_display(2, "Bravo Richard !")
            Tile.gamecontinue = False
        if self.checkpos(e):
            e.message_display(1)
            self.setpos(self.startx, self.starty)
        if self.checkpos(f):
            if t.checkitems(a, b, c):
                self.message_display(1)
                self.setpos(self.startx, self.starty)
                Tile.itemscollected = 0
                a.resetitempos()
                b.resetitempos()
                c.resetitempos()
                t.generateitempos(a, b, c)
            else:
                f.message_display(1)
                f.displayed = False

    def resetitempos(self):
        """Reset positions of items, and inventory items"""
        self.cleanatile("images/way.png")
        self.displayed = True
        self.obtenu = False
        Tile.invstart = 85

    def generateitempos(self, a, b, c):
        """Generate item positions"""
        waylst = []
        ordo = 0
        for x in Tile.level:
            absc = 0
            for y in list(x):
                if y == " ":
                    waylst.append((absc, ordo))
                absc += 40
            ordo += 40
        itemslst = random.sample(waylst, 3)
        itemslst2 = []
        for x in itemslst:
            for y in list(x):
                itemslst2.append(y)
        a.setpos(itemslst2[0], itemslst2[1])
        b.setpos(itemslst2[2], itemslst2[3])
        c.setpos(itemslst2[4], itemslst2[5])

    def score(self):
        """Display the score"""
        color = (255, 255, 255)
        Tile.gamedisplay.blit(
            pygame.font.SysFont(None, 25).render("Objets ramassés: " + str(Tile.itemscollected) +
                                                 "/3", True, color), (420, 570))

    def displayinventory(self):
        """Display the inventory"""
        color = (255, 255, 255)
        Tile.gamedisplay.blit(
            pygame.font.SysFont(None, 25).render("Inventaire : ", True, color), (20, 570))

    def inventorypos(self):
        """Set the coordinates for inventory items"""
        self.invx, self.invy = (Tile.invstart + 40 * Tile.itemscollected), 565

    def displayinventorytile(self):
        sizedimg = pygame.transform.scale(pygame.image.load(self.img), (30, 30))
        Tile.gamedisplay.blit(sizedimg, (self.invx, self.invy))

    def checkinventory(self):
        """Check if inventory should be displayed"""
        if self.obtenu:
            self.displayinventorytile()

    def text_objects(self, text, font):
        """Generate the texts"""
        white = (255, 255, 255)
        textsurface = font.render(text, True, white)
        return textsurface, textsurface.get_rect()

    def message_display(self, temps, text=None):
        """Display the texts"""
        t = Tile()
        if text is None:
            text = self.text
        boximg = pygame.transform.scale(pygame.image.load("images/box.png"), (600, 80))
        Tile.gamedisplay.blit(boximg, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 20)
        textsurf, textrect = self.text_objects(text, largetext)
        textrect.center = (300, 40)
        Tile.gamedisplay.blit(textsurf, textrect)
        pygame.display.update()
        time.sleep(temps)
        t.cleanmessage()

    def cleanmessage(self):
        """Clean the texts"""
        wallimg = pygame.transform.scale(pygame.image.load("images/wall.png"), (40, 40))
        wayimg = pygame.transform.scale(pygame.image.load("images/way.png"), (40, 40))
        lavaimg = pygame.transform.scale(pygame.image.load("images/lava.png"), (40, 40))

        ordo = 0
        i = 0
        while i < 2:
            lst = levels.level2[i]
            absc = 0
            for y in lst:
                if y == " " or "A" or "G" or "M":
                    Tile.gamedisplay.blit(wayimg, (absc, ordo))
                if y == "#":
                    Tile.gamedisplay.blit(wallimg, (absc, ordo))
                if y == "D":
                    Tile.gamedisplay.blit(lavaimg, (absc, ordo))
                absc += 40
            ordo += 40
            i += 1
