from is_figure import *
from collections import Counter
class YamsGame:
    def __init__(self, dice_rolls):
        self.dice_rolls = dice_rolls

    def calculate_score(self):

        final_score = 0

        for roll in self.dice_rolls:
            figures_obtained = []

            if is_brelan(Counter(roll)):
                figures_obtained.append(28)

            if is_carre(Counter(roll)):
                figures_obtained.append(35)

            if is_full(Counter(roll)):
                figures_obtained.append(30)

            if is_grande_suite(sorted(roll)):
                figures_obtained.append(40)

            if is_yams(Counter(roll)):
                figures_obtained.append(50)

            if figures_obtained:
                best_score_roll = max(figures_obtained)
            else:
                best_score_roll = sum(roll)

            final_score += best_score_roll

        return final_score
