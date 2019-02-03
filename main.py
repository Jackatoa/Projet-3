import pygame
from tile import Tile
import niveaux
import random


class Main:
    """Contain all the main functions"""
    jack = Tile()
    jackstart = Tile()
    lava = Tile()
    gardien = Tile()
    syringe = Tile()
    potion = Tile()
    puppet = Tile()
    exit = Tile()
    invsyringe = Tile()
    invpotion = Tile()
    invpuppet = Tile()
    itemscollected = 0
    level = []
    def map(self):
        """Generate all the map tiles"""
        ordo = 0
        for x in Main.level:
            absc = 0
            for y in list(x):
                if y == "#":
                    t.testdisplaytile("images/mur1.png", 40, 40, absc, ordo)
                if y == " ":
                    t.testdisplaytile("images/chemin1.png", 40, 40, absc, ordo)
                if y == "D":
                    t.testdisplaytile("images/lava.png", 40, 40, absc, ordo)
                if y == "A":
                    t.testdisplaytile("images/chemin1.png", 40, 40, absc, ordo)
                if y == "G":
                    t.testdisplaytile("images/chemin1.png", 40, 40, absc, ordo)
                if y == "M":
                    t.testdisplaytile("images/chemin1.png", 40, 40, absc, ordo)
                absc += 40
            ordo += 40

    def getposition(self, indice):
        """Take the indice to return the coordinates """
        ordo = 0
        for x in Main.level:
            absc = 0
            for y in list(x):
                if y == indice:
                    return absc, ordo
                absc += 40
            ordo += 40

    def generationposition(self, indice):
        """Set the coordinates of the specified tile"""
        x, y = m.getposition(indice)
        return x, y

    def generationobjets(self):
        """Take 3 differents random coordinates for the items"""
        waylst = []
        ordo = 0
        for x in Main.level:
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

        m.itemsposreset(itemslst2)
        m.displayitems()

    def itemsposreset(self, list):
        """Set the coordinates for the items"""
        Main.syringe.x = list[0]
        Main.syringe.y = list[1]
        Main.potion.x = list[2]
        Main.potion.y = list[3]
        Main.puppet.x = list[4]
        Main.puppet.y = list[5]
        Main.invsyringe.x = -100
        Main.invsyringe.y = -100
        Main.invpotion.x = -100
        Main.invpotion.y = -100
        Main.invpuppet.x = -100
        Main.invpuppet.y = -100

    def displayitems(self):
        """Display items"""
        t.testdisplaytile("images/potion.png", 40, 40, Main.potion.x, Main.potion.y)
        t.testdisplaytile("images/poupee.png", 40, 40, Main.puppet.x, Main.puppet.y)
        t.testdisplaytile("images/seringue.png", 40, 40, Main.syringe.x, Main.syringe.y)

    def cleanitems(self):
        """Delete the items tiles"""
        t.testdisplaytile("images/chemin1.png", 40, 40, Main.potion.x, Main.potion.y)
        t.testdisplaytile("images/chemin1.png", 40, 40, Main.puppet.x, Main.puppet.y)
        t.testdisplaytile("images/chemin1.png", 40, 40, Main.syringe.x, Main.syringe.y)

    def generationinit(self):
        """Generate all the tiles needed to start the game"""
        m.map()
        m.generationobjets()
        Main.jackstart.x, Main.jackstart.y = m.generationposition("M")
        Main.gardien.x, Main.gardien.y = m.generationposition("G")
        Main.exit.x, Main.exit.y = m.generationposition("A")
        Main.lava.x, Main.lava.y = m.generationposition("D")
        t.testdisplaytile("images/Gardien.png", 40, 40, Main.gardien.x, Main.gardien.y)

    def jackposreset(self):
        """Reset the main character position to the start point"""
        Main.jack.x = Main.jackstart.x
        Main.jack.y = Main.jackstart.y

    def game(self):
        """Main function, make the game run"""
        gamecontinue = True
        m.jackposreset()
        x_change = 0
        y_change = 0
        while gamecontinue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamecontinue = False
                if event.type == pygame.KEYUP:
                    x_change, y_change = m.keyinput(event, Main.jack.x, Main.jack.y)
            t.cleantile(Main.jack.x, Main.jack.y)
            x_change, y_change = m.updatejackpos(x_change, y_change)
            m.refresh()
            if m.checkexit():
                gamecontinue = False
            pygame.display.update()

    def updatejackpos(self, x, y):
        """Update jack coordinates after move"""
        Main.jack.x += x
        Main.jack.y += y
        return 0, 0

    def refresh(self):
        """Get positions and refresh tiles and score"""

        m.checkposition()
        t.cleanscore()
        m.score()
        m.displayinventory()
        t.testdisplaytile("images/MacGyver.png", 40, 40, Main.jack.x, Main.jack.y)

    def score(self):
        """Display the score"""
        color = (255, 255, 255)
        t.testgameDisplay.blit(
            pygame.font.SysFont(None, 25).render("Objets ramassés: " + str(Main.itemscollected) +
                                                 "/3",
                                                 True,
                                                 color),
            (420, 570))

    def keyinputcheck(self, x, y, addx, addy):
        """Return modified coordonates if move is possible"""
        if m.checkmove(x + addx, y + addy):
            return addx, addy
        else:
            return 0, 0

    def keyinput(self, event, x, y):
        """Return coordinates after move tentative"""
        if event.key == pygame.K_LEFT:
            return m.keyinputcheck(x, y, -40, 0)
        if event.key == pygame.K_RIGHT:
            return m.keyinputcheck(x, y, 40, 0)
        if event.key == pygame.K_UP:
            return m.keyinputcheck(x, y, 0, -40)
        if event.key == pygame.K_DOWN:
            return m.keyinputcheck(x, y, 0, 40)

    def itemiscollected(self, item):
        """Store the status of items"""
        item.obtenu = True
        item.x = -100
        item.y = -100
        Main.itemscollected += 1
        m.inventory(item)

    def whereisjack(self, text, item, invitem, time):
        """Check if Jack have picked an item"""
        if (Main.jack.x, Main.jack.y) == (item.x, item.y):
            t.message_display(text, time, 300, 40)
            m.itemiscollected(item)
            m.inventory(invitem)

    def checkbattle(self):
        """Check if Jack have picked all the items to beat the guardian"""
        if Main.puppet.obtenu != True or Main.potion.obtenu != True or Main.syringe.obtenu != True:
            return True

    def checkexit(self):
        """Check if Jack have reach the exit"""
        if (Main.jack.x, Main.jack.y) == (Main.exit.x, Main.exit.y):
            t.message_display("Bravo Richard !", 2, 300, 40)
            return True

    def battleloserestart(self):
        """Reset items and jack"""
        t.message_display("Mal préparé le gardien tire sur richard", 2, 300, 40)
        m.cleanitems()
        m.generationobjets()
        m.jackposreset()
        Main.itemscollected = 0
        Main.syringe.obtenu = False
        Main.potion.obtenu = False
        Main.puppet.obtenu = False

    def displayinventory(self):
        """Display the inventory"""
        color = (255, 255, 255)
        t.testgameDisplay.blit(
            pygame.font.SysFont(None, 25).render("Inventaire : ", True, color), (20, 570))
        t.testdisplaytile("images/poupee.png", 30, 30, Main.invpuppet.x, Main.invpuppet.y)
        t.testdisplaytile("images/seringue.png", 30, 30, Main.invsyringe.x, Main.invsyringe.y)
        t.testdisplaytile("images/potion.png", 30, 30, Main.invpotion.x, Main.invpotion.y)

    def getinventorypos(self):
        """Return coordinates for inventory items"""
        return (85 + 40 * Main.itemscollected), 565

    def inventory(self, item):
        """Set the coordinates for inventory items"""
        item.x, item.y = m.getinventorypos()

    def checkposition(self):
        """Main function to check if Jack is on a same position as an event"""
        m.whereisjack("Une poupée vaudou vampire ? Intéressant...", Main.puppet, Main.invpuppet, 1)
        m.whereisjack("Une bouteille rempli de sang... ", Main.potion, Main.invpotion, 1)
        m.whereisjack("Une seringue vide...", Main.syringe, Main.invsyringe, 1)
        if (Main.jack.x, Main.jack.y) == (Main.lava.x, Main.lava.y):
            t.message_display("Tu aurais du apporter des saucisses", 1, 300, 40)
            m.jackposreset()
        if (Main.jack.x, Main.jack.y) == (Main.gardien.x, Main.gardien.y):
            if m.checkbattle():
                m.battleloserestart()
            else:
                t.message_display("Le gardien prends sa pause café", 2, 300, 40)
                Main.gardien.x = -100
                Main.gardien.y = -100

    def checkmove(self, x, y):
        """Check if the move is possible"""
        ordo = 0
        walllst = []
        for a in Main.level:
            absc = 0
            for b in list(a):
                if b == "#":
                    walllst.append((absc, ordo))
                absc += 40
            ordo += 40
        if (x, y) not in walllst:
            return True


pygame.init()

clock = pygame.time.Clock()
clock.tick(60)
Main.level = niveaux.niveau2
t = Tile()
m = Main()
m.generationinit()
m.game()

pygame.quit()
quit()
