import random


class options():
    p_count = 0
    what_player_is_dealer = 0
    def get(self):
        while True:
            # get valid player count
            try:
                self.p_count = int(input("Player Count (1-4): "))
                if self.p_count < 1 or self.p_count > 4:
                    continue
                break
            except:
                continue
        
        while True:
            # get valid dealer player number
            try:
                self.what_player_is_dealer = int(input("Number of Player that is dealer (1-4): "))
                if self.what_player_is_dealer < 1 or self.what_player_is_dealer > self.p_count:
                    continue
                break
            except:
                continue