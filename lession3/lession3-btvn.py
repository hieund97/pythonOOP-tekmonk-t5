
# đề bài: https://docs.google.com/document/d/1EKpaQ-fkwRbpviCY9LcHBTNIRhZwmcqIKkC_gl9Ta9Y/edit

import random

class Game:
    def __init__(self, game_type):
        self.type = game_type
        self.score_list = []
        
    @property
    def score(self):
        if self.type == "dice":
            return random.randint(1, 6)
        elif self.type == "coin":
            return random.choice([0, 1])
        
    @property
    def quantity(self):
        return len(self.score_list)
    
    @quantity.setter
    def quantity(self, new_quantity):
        for _ in range(new_quantity):
            self.score_list.append(self.score)

    @quantity.deleter
    def quantity(self):
        self.score_list = []
    
    @property
    def total_score(self):
        return sum(self.score_list)
    
    def play(self, quantity = 0):
        del self.quantity
        self.quantity = quantity
        print(f"Score: {self.quantity} | Plays: {self.type} : {self.score_list} | Total scores: {self.type} {self.total_score}")
        
# Create game instances
game1 = Game("dice")
game2 = Game("coin")

# Play the games
game1.play(quantity=3)

game2.play(quantity=5)

# Display total and number of plays
print("Game 1 (Dice):")
print(f"Total plays: {game1.quantity}")
print(f"Total score: {game1.total_score}")

print("Game 2 (Coin):")
print(f"Total plays: {game2.quantity}")
print(f"Total score: {game2.total_score}")
