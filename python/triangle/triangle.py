def is_equilateral(sides):
    """ Return True if triangle is equilateral, otherwise return False """
    if len(list(set(sides))) == 1 and is_triangle(sides):
        return True
    return False


def is_isosceles(sides):
    """ Return True if triangle is isosceles, otherwise return False """
    if len(list(set(sides))) < 3 and is_triangle(sides):
        return True
    return False


def is_scalene(sides):
    """ Return True if triangle is scalene, otherwise return False """
    if len(list(set(sides))) == 3 and is_triangle(sides):
        return True
    return False


def is_triangle(s):
    """ Return True if from sides 's' can be created triangle, otherwise return False """
    r = list(filter(lambda x: x > 0, s))
    if len(r) == 3 and is_properly_length_of_sides(s):
        return True
    return False


def is_properly_length_of_sides(s):
    """ Return True if length of triangle sides 's' have correct value, otherwise return False """
    longest_side = max(s)
    s.remove(longest_side)
    if sum(s) > longest_side:
        return True
    return False
