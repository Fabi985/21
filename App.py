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
        self.Game_round = 0
        self.Game_running = True
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
        print(f"game rounds: {self.Game_round} Game turns: {self.Game_loop_turns}\n")
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
        self.Game_loop_turns = 0
        #TODO: 
        #Add multiple rounds
        #save choices for hitting or standing
        for i in range(2):
            for index, player in enumerate(self.Players):
                    random_card_from_dealer = random.choice(self.Dealer.Dealer_cards)
                    if i == 0:
                        player.Private_card = random_card_from_dealer
                    elif i == 1:
                        player.Public_cards.append(random_card_from_dealer)
                    self.Dealer.Dealer_cards.remove(random_card_from_dealer)

        while self.Player1.stand == False or self.Player2.stand == False:
            self.Display_info()
            print(f"\nDealer cards left: {self.Dealer.Dealer_cards}")
            print(len(self.Dealer.Dealer_cards))
            print(self.Player1.stand)
            print(self.Player2.stand)
            for index, player in enumerate(self.Players):
                player.Private_total = player.Private_card
                player.Public_total = sum(player.Public_cards)
                player.total_cards = sum(player.Public_cards) + player.Private_card
            if self.Player1.turn == True:
                while True:
                    print(f"{self.Color_text("GREEN", f"{self.Player1.name} pick an option:")}")
                    print("1 - Hit\n2 - Stand")
                    choice = int(input("\n>>>"))
                    if choice == 1:
                        random_card_from_dealer = random.choice(self.Dealer.Dealer_cards)
                        self.Player1.Public_cards.append(random_card_from_dealer)
                        self.Dealer.Dealer_cards.remove(random_card_from_dealer)
                        self.Player1.stand = False
                        break
                    elif choice == 2:
                        self.Player1.stand = True
                        break
                    else:
                        print("error 1")

                self.Player1.turn = False
                self.Player2.turn = True
            elif self.Player2.turn == True:
                #TODO: get the npc to choose
                print(f"{self.Color_text("BLUE", f"{self.Player2.name} pick an option:")}")
                choice = self.Player2.Choose(self.Player1.Public_total)
                print(f"NPC choice: {choice}")
                if choice == 1:
                    random_card_from_dealer = random.choice(self.Dealer.Dealer_cards)
                    self.Player2.Public_cards.append(random_card_from_dealer)
                    self.Dealer.Dealer_cards.remove(random_card_from_dealer)
                    self.Player2.stand = False
                elif choice == 2:
                    self.Player2.stand = True
                else:
                    print("fuck")

                self.Player2.turn = False
                self.Player1.turn = True
            
            self.Game_loop_turns += 1
        
        self.Check_cards()
        self.End_round()

    def Check_cards(self):
        player_1_total = self.Player1.total_cards
        player_2_total = self.Player2.total_cards
        player_1_win = 2
        player_2_win = 1
        both_lose = 3
        #TODO:make lucas baker announce winner and loser
        print(f"Total player1: {player_1_total}, total player2: {player_2_total}")
        if player_1_total == 21:
            self.Player_wins(player_1_win)
        elif player_2_total == 21:
            self.Player_wins(player_2_win)
        elif player_1_total <= 21 and player_2_total > 21:
            self.Player_wins(player_1_win)
        elif player_2_total <= 21 and player_1_total > 21:
            self.Player_wins(player_2_win)
        elif player_1_total > player_2_total and player_1_total <= 21:
            self.Player_wins(player_1_win)
        elif player_2_total > player_1_total and player_2_total <= 21:
            self.Player_wins(player_2_win)
        elif player_1_total > 21 and player_2_total > 21:
            self.Player_wins(both_lose)
        pass

    def Player_wins(self, loser):
        if loser == 1:
            print("Player 1 lost, player 2 win")
            self.Player1.health -= self.Dealer.Hurt_power
            self.Player1.turn = False
            self.Player2.turn = True
        elif loser == 2:
            print("Player 1 won, player 2 lost")
            self.Player2.health -= self.Dealer.Hurt_power
            self.Player1.turn = True
            self.Player2.turn = False
        elif loser == 3:
            print("You both lost, fucking losers")
            for index, player in enumerate(self.Players):
                player.health -= self.Dealer.Hurt_power
    
    def End_round(self):
        self.Game_round += 1
        self.Dealer.Hurt_power += 2
        self.Dealer.Dealer_cards = self.Dealer.Dealer_deck_copied.copy()
        for index, player in enumerate(self.Players):
            player.stand = False
            player.Private_card = 0
            player.Public_cards = []
            player.Private_total = 0
            player.Public_total = 0
            player.total_cards = 0
        print(f"Testing gahh\n\n{self.Dealer.Dealer_cards}, {self.Dealer.Hurt_power}")
        self.Stall()
        self.Check_health()
        if self.Game_running == True:
            self.Game_loop()
        elif self.Game_running == False:
            self.Game_end()
    
    def Check_health(self):
        #TODO: if a player has < 0 health then the game has ended and they lost
        if self.Player1.health <= 0:
            print("Player1 died lmao")
            self.Game_running = False
        elif self.Player2.health <= 0:
            print("Player2 died lmao")
            self.Game_running = False
        elif self.Player1.health <= 0 and self.Player2.health <= 0:
            print("yall both died, fuck you")
            self.Game_running = False
        else:
            self.Game_running = True
        pass

    def Game_end(self):
        print("Game ended")

    
if __name__ == "__main__":
    App_start = App()
    App_start.Game_setup()