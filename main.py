import pygame
from tile import Tile
from character import Character
from item import Item
import random


class Main:
    gamecontinue = True
    maplist = [line.rstrip('\n') for line in open('levels.txt')]
    lava = Tile("images/lava.png", "Tu aurais du apporter des saucisses !")
    exit = Tile("", "Bravo Richard !")
    gardian = Tile("images/gardien.png", "Le gardien prend sa pause café")
    jack = Character("images/MacGyver.png", "Le gardien tire sur Richard")
    potion = Item("images/potion.png", "Une bouteille remplie de sang...")
    puppet = Item("images/poupee.png", "Une poupée vaudou vampire ? Intéressant...")
    syringe = Item("images/seringue.png", "Une seringue vide...")

    def game(self):
        m.display_world()
        pygame.display.update()
        while Main.gamecontinue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Main.gamecontinue = False
                if event.type == pygame.KEYUP:
                    Main.jack.key_input(event)
                    m.check_events()
                    m.display_world()
                    pygame.display.update()

    def generate_main_tiles_pos(self):
        ordo = 0
        for x in Main.maplist:
            absc = 0
            for y in list(x):
                if y == "M":
                    Main.jack.set_starting_pos(absc, ordo)
                if y == "G":
                    Main.gardian.set_pos(absc, ordo)
                if y == "A":
                    Main.exit.set_pos(absc, ordo)
                absc += 40
            ordo += 40

    def generate_items_pos(self):
        ordo = 0
        waylst = []
        for a in Main.maplist:
            absc = 0
            for b in list(a):
                if b == " ":
                    waylst.append((absc, ordo))
                absc += 40
            ordo += 40
        waylst = random.sample(waylst, 3)
        Main.syringe.set_pos(*waylst[0])
        Main.puppet.set_pos(*waylst[1])
        Main.potion.set_pos(*waylst[2])

    def generate_pos(self):
        m.generate_main_tiles_pos()
        m.generate_items_pos()

    def generate_map(self):
        way = Tile("images/way.png")
        wall = Tile("images/wall.png")
        ordo = 0
        for x in Main.maplist:
            absc = 0
            for y in list(x):
                if y == "M" or y == "G" or y == " " or y == "A":
                    way.set_pos(absc, ordo)
                    way.display()
                elif y == "D":
                    Main.lava.set_pos(absc, ordo)
                    Main.lava.display()
                elif y == "#":
                    wall.set_pos(absc, ordo)
                    wall.display()
                absc += 40
            ordo += 40

    def check_item_event(self):
        lstitems = [Main.potion, Main.puppet, Main.syringe]
        for item in lstitems:
            Main.jack.is_jack_on_item(item)

    def check_tile_event(self):
        if Main.jack.get_pos() == Main.exit.get_pos():
            Main.gamecontinue = False
            Main.exit.message_display_text(2)
        if Main.jack.get_pos() == Main.lava.get_pos():
            Main.jack.go_to_start()
            Main.lava.message_display_text(1)
        if Main.jack.get_pos() == Main.gardian.get_pos():
            if Item.itemscollected != 3:
                Item.itemscollected = 0
                Main.puppet.reset_item()
                Main.syringe.reset_item()
                Main.potion.reset_item()
                m.generate_pos()
                Main.jack.message_display_text(2)
            else:
                Main.gardian.message_display_text(2)
                Main.gardian.displayed = False

    def check_events(self):
        m.check_item_event()
        m.check_tile_event()

    def score(self):
        color = (255, 255, 255)
        Tile.gamedisplay.blit(
            pygame.font.SysFont(None, 25).render("Objets ramassés: " + str(Item.itemscollected) +
                                                 "/3", True, color), (420, 570))

    def inventory(self):
        """Inventory text"""
        color = (255, 255, 255)
        Tile.gamedisplay.blit(
            pygame.font.SysFont(None, 25).render("Inventaire : ", True, color), (20, 570))

    def display_world(self):
        lstitems = [Main.potion, Main.puppet, Main.syringe]
        t.clean_ui()
        for x in lstitems:
            x.should_it_be_displayed()
            x.should_inv_be_displayed()
        Main.gardian.should_it_be_displayed()
        m.score()
        m.inventory()
        Main.jack.display()


pygame.init()

clock = pygame.time.Clock()
clock.tick(60)
t = Tile()
m = Main()

m.generate_pos()
m.generate_map()
m.game()

pygame.quit()
quit()
