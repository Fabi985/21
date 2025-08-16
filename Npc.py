class Npc(object):
    def __init__(self):
        self.ID = 0
        self.TYPE = "NPC"

        self.name = "Hoffman"
        self.health = 10
        self.turn = False
        self.stand = False

        self.Private_card = 0
        self.Public_cards = []
        self.Special = []
        
        self.Private_total = 0
        self.Public_total = 0
        self.total_cards = 0
    
    def Choose(self, player1_public_cards):
        choice = 0
        player_1_total = player1_public_cards
        player_2_total = self.total_cards
        print(player_1_total, player_2_total)
        if 17 <= player_2_total <= 21:
            choice = 2
        elif player_2_total > 21 or player_2_total == 21:
            choice = 2
        elif player_2_total < 21:
            choice = 1

        return choice
    