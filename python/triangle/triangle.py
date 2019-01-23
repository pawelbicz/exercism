def is_equilateral(sides):
    if is_triangle(sides) is not True:
        return False
    if len(list(set(sides))) == 1:
        return True
    return False


def is_isosceles(sides):
    if is_triangle(sides) is not True:
        return False
    if len(list(set(sides))) < 3:
        return True
    return False


def is_scalene(sides):
    pass


def is_triangle(s):
    r = list(filter(lambda x: x > 0, s))
    if len(r) == 3:
        return True
    return False

print(is_isosceles([4, 4, 4]))