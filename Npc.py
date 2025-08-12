class Npc(object):
    def __init__(self):
        self.ID = 0
        self.TYPE = "NPC"

        self.name = "Hoffman"
        self.health = 10
        self.turn = False

        self.Private_card = []
        self.Public_cards = []
        self.Special = []
        
        self.Private_total = 0
        self.Public_total = 0
    