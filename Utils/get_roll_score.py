from .is_figure import *
from collections import Counter


def get_roll_score(roll):
    figures_score_obtained = []

    if is_brelan(Counter(roll)):
        figures_score_obtained.append(28)

    if is_carre(Counter(roll)):
        figures_score_obtained.append(35)

    if is_full(Counter(roll)):
        figures_score_obtained.append(30)

    if is_grande_suite(sorted(roll)):
        figures_score_obtained.append(40)

    if is_yams(Counter(roll)):
        figures_score_obtained.append(50)

    if figures_score_obtained:
        best_score_roll = max(figures_score_obtained)
    else:
        best_score_roll = sum(roll)

    return best_score_roll
