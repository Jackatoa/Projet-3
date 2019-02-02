import pygame
from tile import Tile
import niveaux
import random

"""
AFFICHAGE
    affichage de la map
    affichage des objets
    affichage du gardien
    affichage de jack
    affichage de l'inventaire'
    affichage du score

generation de la map
    labyrinthe
    position de base des personnages
    position de base des objets



Jeu
    interaction avec les touches
        checkmove

    checkposition
        position des objets
        sortie
        gardien
        lave

    refresh images
        refresh de la position de mc gyver
        refresh des objets
        refresh du compteur
        refresh du gardien
        refresh des messages"""


class Main:
    jack = Tile()
    jackstart = Tile()
    lava = Tile()
    gardien = Tile()
    syringe = Tile()
    potion = Tile()
    puppet = Tile()
    exit = Tile()
    itemscollected = 0

    def map(self):
        ordo = 0
        for x in niveaux.niveau2:
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
        ordo = 0
        for x in niveaux.niveau2:
            absc = 0
            for y in list(x):
                if y == indice:
                    return absc, ordo
                absc += 40
            ordo += 40

    def generationposition(self, indice):
        x, y = m.getposition(indice)
        return x, y

    def generationobjets(self):
        waylst = []
        ordo = 0
        for x in niveaux.niveau2:
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

        Main.syringe.x = itemslst2[0]
        Main.syringe.y = itemslst2[1]
        Main.potion.x = itemslst2[2]
        Main.potion.y = itemslst2[3]
        Main.puppet.x = itemslst2[4]
        Main.puppet.y = itemslst2[5]
        m.displayitems()

    def displayitems(self):
        t.testdisplaytile("images/potion.png", 40, 40, Main.potion.x, Main.potion.y)
        t.testdisplaytile("images/seringue.png", 40, 40, Main.puppet.x, Main.puppet.y)
        t.testdisplaytile("images/poupee.png", 40, 40, Main.syringe.x, Main.syringe.y)

    def cleanitems(self):
        t.testdisplaytile("images/chemin1.png", 40, 40, Main.potion.x, Main.potion.y)
        t.testdisplaytile("images/chemin1.png", 40, 40, Main.puppet.x, Main.puppet.y)
        t.testdisplaytile("images/chemin1.png", 40, 40, Main.syringe.x, Main.syringe.y)

    def generationinit(self):
        m.map()
        m.generationobjets()
        Main.jackstart.x, Main.jackstart.y = m.generationposition("M")
        Main.gardien.x, Main.gardien.y = m.generationposition("G")
        Main.exit.x, Main.exit.y = m.generationposition("A")
        Main.lava.x, Main.lava.y = m.generationposition("D")
        t.testdisplaytile("images/Gardien.png", 40, 40, Main.gardien.x, Main.gardien.y)



    def game(self):
        gamecontinue = True
        Main.jack.x = Main.jackstart.x
        Main.jack.y = Main.jackstart.y
        x_change = 0
        y_change = 0
        while gamecontinue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamecontinue = False
                if event.type == pygame.KEYUP:
                    x_change, y_change = m.keyinput(event, Main.jack.x, Main.jack.y)
            t.cleantile(Main.jack.x, Main.jack.y)
            Main.jack.x += x_change
            x_change = 0
            Main.jack.y += y_change
            y_change = 0
            m.checkposition()
            if m.checkposition():
                gamecontinue = False
            t.testdisplaytile("images/MacGyver.png", 40, 40, Main.jack.x, Main.jack.y)
            pygame.display.update()

    def keyinput(self, event, x, y):
        if event.key == pygame.K_LEFT:
            if m.checkmove(x - 40, y, ):
                return -40, 0
            else:
                return 0, 0
        if event.key == pygame.K_RIGHT:
            if m.checkmove(x + 40, y):
                return 40, 0
            else:
                return 0, 0
        if event.key == pygame.K_UP:
            if m.checkmove(x, y - 40):
                return 0, -40
            else:
                return 0, 0
        if event.key == pygame.K_DOWN:
            if m.checkmove(x, y + 40):
                return 0, 40
            else:
                return 0, 0

    def itemiscollected(self, item):
        # collecte les objets
        item.obtenu = True
        item.x = -100
        item.y = -100
        Main.itemscollected += 1

    def whereisjack(self, text, item, time):
        # compare la position de Jack aux objets, affichant un message et les ramassants
        if (Main.jack.x, Main.jack.y) == (item.x, item.y):
            t.message_display(text, time, 300, 40)
            m.itemiscollected(item)

    def checkbattle(self):
        # vérifie que les conditions requises sont remplies pour endormir le gardien
        if Main.puppet.obtenu != True or Main.potion.obtenu != True or Main.syringe.obtenu != True:
            return True

    def checkposition(self):
        # compare la position de McGyver aux objets / personnages
        m.whereisjack("Une poupée vaudou vampire ? Intéressant...", Main.puppet, 1)
        m.whereisjack("Une bouteille rempli de sang... Mais du sang de quoi ?", Main.potion, 1)
        m.whereisjack("Une seringue vide...", Main.syringe, 1)

        if (Main.jack.x, Main.jack.y) == (Main.exit.x, Main.exit.y):
            t.message_display("Bravo Richard !", 2, 300, 40)
            return True
        if (Main.jack.x, Main.jack.y) == (Main.lava.x, Main.lava.y):
            t.message_display("Tu aurais du apporter des saucisses", 1, 300, 40)
            Main.jack.x = Main.jackstart.x
            Main.jack.y = Main.jackstart.y
        if (Main.jack.x, Main.jack.y) == (Main.gardien.x, Main.gardien.y):
            if m.checkbattle():
                t.message_display("Mal préparé le gardien tire sur richard", 2, 300, 40)
                m.cleanitems()
                m.generationobjets()
                Main.jack.x = Main.jackstart.x
                Main.jack.y = Main.jackstart.y
            else:
                t.message_display("Le gardien prends sa pause café", 2, 300, 40)
                Main.gardien.x = -100
                Main.gardien.y = -100

    def checkmove(self, x, y):
        ordo = 0
        walllst = []
        for a in niveaux.niveau2:
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
t = Tile()
m = Main()
m.generationinit()
m.game()

pygame.quit()
quit()
