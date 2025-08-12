class Player(object):
    def __init__(self):
        self.ID = 0
        self.TYPE = "player"

        self.name = "Clancy"
        self.health = 10
        self.turn = False

        self.Private_card = 0
        self.Public_cards = []
        self.Special = []
        
        self.Private_total = 0
        self.Public_total = 0
    
    def Rename(self):
        #TODO: Redo this so they have to change theyre name
        if self.ID == 0:
            print("First player enter your name")
        elif self.ID == 1:
            print("Second player enter your name")
        validate = input(">>>")
        if validate == "":
            pass
        else:
            self.name = validate
    