def is_equilateral(sides):
    result = list(filter(lambda x: x == sides[0], sides))
    if len(result) == 3:
        return True
    return False


def is_isosceles(sides):
    pass


def is_scalene(sides):
    pass
