from Utils.get_roll_score import *
class YamsGame:
    def __init__(self, dice_rolls):
        self.dice_rolls = dice_rolls

    def calculate_score(self):

        final_score = 0

        for roll in self.dice_rolls:
            final_score += get_roll_score(roll)

        return final_score
