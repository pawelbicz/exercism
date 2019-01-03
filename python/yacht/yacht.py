# Score categories
# Change the values as you see fit
YACHT = lambda d: 50 if len(set(d)) == 1 else 0
ONES = lambda d: d.count(1) * 1
TWOS = lambda d: d.count(2) * 2
THREES = lambda d: d.count(3) * 3
FOURS = lambda d: d.count(4) * 4
FIVES = lambda d: d.count(5) * 5
SIXES = lambda d: d.count(6) * 6
FULL_HOUSE = lambda d: check_full_of_house(d)
FOUR_OF_A_KIND = lambda d: calc_total_of_fourth_of_kind(d)
LITTLE_STRAIGHT = lambda d: 30 if sorted(d) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda d: 30 if sorted(d) == [2, 3, 4, 5, 6] else 0
CHOICE = lambda d: sum(d)


def score(dice, category):
    if any(not 0 < x < 7 for x in dice) and len(dice) != 5:
        raise ValueError("Incorrect number/format of dice")
    print(category(dice))
    return category(dice)


def check_full_of_house(d):
    sorted_d = (sorted(d))
    value = 0
    first = sorted_d.count(sorted_d[0])
    last = sorted_d.count(sorted_d[-1])
    if first + last == 5:
        if first == 2:
            value = sorted_d[0] * 2 + sorted_d[-1] * 3
        elif first == 3:
            value = sorted_d[0] * 3 + sorted_d[-1] * 2
        else:
            print('No FULL OF HOUSE')
    else:
        print("No full of house")
    return value


def calc_total_of_fourth_of_kind(d):
    d = sorted(d)
    value = 0
    if d.count(d[1]) == 4 or d.count(d[1]) == 5:
        value = d[1] * 4
    else:
        print('No four identical value in dice')
    return value
