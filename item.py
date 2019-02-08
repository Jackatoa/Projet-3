from tile import Tile


class Item(Tile):
    itemscollected = 0

    def __init__(self, img, text):
        Tile.__init__(self, img, text)
        self.collected = False
        self.invx = -100
        self.invy = -100

    def set_inventory_pos(self, x, y):
        self.invx = x
        self.invy = y

    def item_event(self):
        self.collected = True
        self.displayed = False
        self.get_inventory_pos()
        Item.itemscollected += 1
        self.clean_a_tile()
        self.clean_a_tile("images/MacGyver.png")
        self.message_display_text(1)

    def display_inventory(self):
        """Display a tile"""
        Tile.gamedisplay.blit(self.get_sized(30, 30), (self.invx, self.invy))

    def should_inv_be_displayed(self):
        if self.collected:
            self.display_inventory()

    def get_inventory_pos(self):
        self.set_inventory_pos(125 + 40 * Item.itemscollected, 565)

    def reset_item(self):
        self.collected = False
        self.displayed = True
        self.clean_ui()
