def is_equilateral(sides):
    if is_triangle(sides) is not True:
        return False
    result = list(filter(lambda x: x == sides[0], sides))
    if len(result) == 3:
        return True
    return False


def is_isosceles(sides):
    pass


def is_scalene(sides):
    pass


def is_triangle(s):
    r = list(filter(lambda x: x >0 , s))
    if len(r) == 3:
        return True
    return False