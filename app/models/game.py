class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
        



    def play_game(self):
            
        if self.player1.selection == self.player2.selection:
            return "Tie!"
        elif self.player1.selection == "Rock":
            if self.player2.selection == "Paper":
                return "You chose Rock, you lose"
            else:
                return "You chose Rock, you win!"
        elif self.player1.selection == "Paper":
            if self.player2.selection == "Scissors":
                return "You chose Paper, you lose"
            else:
                return "You chose Paper, you win"
        elif self.player1.selection == "Scissors":
            if self.player2.selection == "Rock":
                return "You chose Scissors, you lose"
            else:
                return "You chose Scissors, you win"
        else:
            return "try again"



