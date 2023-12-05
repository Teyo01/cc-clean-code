def is_brelan(roll_counter):
    if 3 in roll_counter.values():
        return True


def is_carre(roll_counter):
    if 4 in roll_counter.values():
        return True


def is_full(roll_counter):
    if set(roll_counter.values()) == {2, 3}:
        return True


def is_grande_suite(sorted_roll):
    if set(sorted_roll) == {1, 2, 3, 4, 5} or set(sorted_roll) == {2, 3, 4, 5, 6}:
        return True


def is_yams(roll_counter):
    if 5 in roll_counter.values():
        return True
