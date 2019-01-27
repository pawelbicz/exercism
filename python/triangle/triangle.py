def is_equilateral(sides):
    if len(list(set(sides))) == 1 and is_triangle(sides):
        return True
    return False


def is_isosceles(sides):
    if len(list(set(sides))) < 3 and is_triangle(sides):
        return True
    return False


def is_scalene(sides):
    if len(list(set(sides))) == 3 and is_triangle(sides):
        return True
    return False


def is_triangle(s):
    r = list(filter(lambda x: x > 0, s))
    if len(r) == 3 and is_properly_length_of_sides(s):
        return True
    return False


def is_properly_length_of_sides(s):
    longest_side = max(s)
    s.remove(longest_side)
    if sum(s) > longest_side:
        return True
    return False
