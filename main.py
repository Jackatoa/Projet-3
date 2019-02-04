import pygame
from tile import Tile
import levels


class Main:
    """Main Class"""
    jack = Tile("images/MacGyver.png", "Le gardien tire sur Richard")
    lava = Tile("images/lava.png", "Tu aurais du apporter des saucisses")
    guardian = Tile("images/guardian.png", "Le gardien prends sa pause café")
    syringe = Tile("images/seringue.png", "Une seringue vide...")
    potion = Tile("images/potion.png", "Une bouteille rempli de sang... ")
    puppet = Tile("images/poupee.png", "Une poupée vaudou vampire ? Intéressant...")
    exit = Tile("images/way.png", "Bravo Richard !")
    wall = Tile("images/wall.png")
    way = Tile("images/way.png")

    def game(self):
        """Main game function"""
        m.displayworld()
        pygame.display.update()
        while Tile.gamecontinue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Tile.gamecontinue = False
                if event.type == pygame.KEYUP:
                    Main.jack.keyinput(event)
                    Main.jack.checkposevent(Main.puppet, Main.syringe, Main.potion, Main.exit,
                                            Main.lava, Main.guardian)
                    m.displayworld()
                    pygame.display.update()

    def map(self):
        """Generate the map"""
        ordo = 0
        for x in Tile.level:
            absc = 0
            for y in list(x):
                if y == "#":
                    Main.wall.setpos(absc, ordo)
                    Main.wall.display()
                elif y == "D":
                    Main.lava.setpos(absc, ordo)
                    Main.lava.display()
                else:
                    Main.way.setpos(absc, ordo)
                    Main.way.display()
                absc += 40
            ordo += 40

    def displayworld(self):
        """Display chars, items, score, inventory"""
        m.cleanscore()
        Main.jack.shoulditbedisplayed()
        Main.guardian.shoulditbedisplayed()
        Main.potion.shoulditbedisplayed()
        Main.syringe.shoulditbedisplayed()
        Main.puppet.shoulditbedisplayed()
        Main.potion.checkinventory()
        Main.syringe.checkinventory()
        Main.puppet.checkinventory()
        t.displayinventory()
        t.score()

    def generateposition(self):
        """Generate positions of char and events"""
        t.generateitempos(Main.potion, Main.syringe, Main.puppet)
        ordo = 0
        for x in Tile.level:
            absc = 0
            for y in list(x):
                if y == "M":
                    Main.jack.startx = absc
                    Main.jack.starty = ordo
                    Main.jack.setpos(absc, ordo)
                if y == "G":
                    Main.guardian.setpos(absc, ordo)
                if y == "D":
                    Main.lava.setpos(absc, ordo)
                if y == "A":
                    Main.exit.setpos(absc, ordo)
                absc += 40
            ordo += 40

    def cleanscore(self):
        """Clean the score"""
        ordo = 560
        lst = niveaux.niveau2[14]
        absc = 0
        for y in lst:
            if y == "#":
                Main.wall.setpos(absc, ordo)
                Main.wall.display()
            if y == " ":
                Main.wall.setpos(absc, ordo)
                Main.wall.display()
            absc += 40


pygame.init()

clock = pygame.time.Clock()
clock.tick(60)
Tile.level = levels.level2
t = Tile()
m = Main()
m.generateposition()
m.map()
m.game()

pygame.quit()
quit()
