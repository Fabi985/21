from Player import *
from Dealer import *
import random
from colorama import init, Fore, Back, Style

class App:
    def __init__(self):
        init()
        self.Player1 = Player()
        self.Player2 = self.Select_opponent()
        self.Players = [self.Player1, self.Player2]

        self.Dealer = Dealer()
        pass

    def Select_opponent(self):
        print("""\nWelcome to Twenty one \n\nSelect an opponent: """)
        while True:
            print("""
1 - NPC
2 - IRL""")
            User_choice = int(input("\n>>>"))
            if User_choice == 1:
                Player2 = "Npc()"
                break
            elif User_choice == 2:
                Player2 = Player()
                break
            else:
                print("Not an option")

        return Player2

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
                    print(f"{self.Color_text("GREEN", f"{player.name}'s turn")}")
                elif index == 1:
                    print(f"{self.Color_text("BLUE", f"{player.name}'s turn")}")
        for index, player in enumerate(self.Players):
            if index == 0:
                print(f"\n{self.Color_text("GREEN", f"Player name: {player.name}")}, \nHealth remaining: {player.health}")
            elif index == 1:
                print(f"\n{self.Color_text("BLUE", f"Player name: {player.name}")}, \nHealth remaining: {player.health}")
    
    def Choose_starter_turn(self):
        choice = random.randint(1,2)
        if choice == 1:
            self.Player1.turn = True
        elif choice == 2:
            self.Player2.turn = True
        else:
            print("Fuck we had an error")
    
    def Game_loop(self):
        while self.Player1.health > 0 or self.Player2.health > 0:
            self.Display_info()
            self.Stall()


    
if __name__ == "__main__":
    App_start = App()
    App_start.Game_setup()