from Player import *
from Npc import *
from Dealer import *
import random
from colorama import init, Fore, Back, Style

class App:
    def __init__(self):
        init()
        self.Player1 = Player()
        self.Player2 = Npc()
        self.Players = [self.Player1, self.Player2]

        self.Dealer = Dealer()
        pass

    def Stall(self):
        return input("\nPress [ENTER] to continue")

    def Color_text(self, color, text):
        if color == "GREEN":
            return f"{Fore.GREEN}{text}{Fore.WHITE}"
        elif color == "RED":
            return f"{Fore.RED}{text}{Fore.WHITE}"
        elif color == "BLUE":
            return f"{Fore.BLUE}{text}{Fore.WHITE}"
        elif color == "WHITE":
            return f"{Fore.WHITE}"
        pass

    def Game_setup(self):
        # Rename
        for index, player in enumerate(self.Players):
            player.ID = index
            if player.TYPE == "player":
                player.Rename()
                print(chr(27) + "[2J")
            else:
                pass

        # Game startup
        self.Choose_starter_turn()    
        self.Game_loop()
        
    def Display_info(self):
        print(chr(27) + "[2J")
        print("Game Info:\n")
        print(f"{self.Color_text("RED", f"Dealer name: {self.Dealer.name}, Hurt Power: {self.Dealer.Hurt_power}")}")
        for index, player in enumerate(self.Players):
            if player.turn == True:
                if index == 0:
                    color = "GREEN"
                elif index == 1:
                    color = "BLUE"
                print(f"{self.Color_text(color, f"{player.name}'s turn")}")
        for index, player in enumerate(self.Players):
            if index == 0:
                print(f"\n{self.Color_text("GREEN", f"Player name: {player.name}")}, \nHealth remaining: {player.health}")
                print(f"{player.name}'s private card: {player.Private_card}, Public cards: {player.Public_cards}\ntotal: {int(player.Private_card) + sum(player.Public_cards)}/21")
            elif index == 1:
                print(f"\n{self.Color_text("BLUE", f"Player name: {player.name}")}, \nHealth remaining: {player.health}")
                print(f"{player.name}'s private card: ???({player.Private_card}), Public cards: {player.Public_cards}\ntotal: ???+{sum(player.Public_cards)}({int(player.Private_card) + sum(player.Public_cards)})/21")
            
    
    def Choose_starter_turn(self):
        choice = random.randint(1,2)
        if choice == 1:
            self.Player1.turn = True
        elif choice == 2:
            self.Player2.turn = True
        else:
            print("Fuck we had an error")
    
    def Game_loop(self):
        #TODO: 
        #Add multiple rounds
        #save choices for hitting or standing
        #If both stand then finish round
        for i in range(2):
            for index, player in enumerate(self.Players):
                    random_card_from_dealer = random.choice(self.Dealer.Dealer_cards)
                    if i == 0:
                        player.Private_card = random_card_from_dealer
                    elif i == 1:
                        player.Public_cards.append(random_card_from_dealer)
                    self.Dealer.Dealer_cards.remove(random_card_from_dealer)

        while self.Player1.health > 0 or self.Player2.health > 0:
            self.Display_info()
            if self.Player1.turn == True:
                while True:
                    try:
                        print(f"{self.Color_text("GREEN", f"{self.Player1.name} pick an option:")}")
                        print("1 - Hit\n2 - Stand")
                        choice = int(input("\n>>>"))
                        if choice == 1:
                            random_card_from_dealer = random.choice(self.Dealer.Dealer_cards)
                            self.Player1.Public_cards.append(random_card_from_dealer)
                            self.Dealer.Dealer_cards.remove(random_card_from_dealer)
                            break
                        elif choice == 2:
                            pass
                            break
                        else:
                            print("error 1")
                    except:
                        print("Not a thing try again")

                self.Player1.turn = False
                self.Player2.turn = True
                pass
            elif self.Player2.turn == True:
                #TODO: get the npc to choose
                print(f"{self.Color_text("BLUE", f"{self.Player2.name} pick an option:")}")

                self.Player2.turn = False
                self.Player1.turn = True

            print(f"\nDealer cards left: {self.Dealer.Dealer_cards}")
            self.Stall()



    
if __name__ == "__main__":
    App_start = App()
    App_start.Game_setup()