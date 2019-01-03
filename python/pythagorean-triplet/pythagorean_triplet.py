import itertools


def triplets_with_sum(sum):
    sides_of_triangle = []
    for a, b in itertools.product(range(int(sum/3.5)), range(int(sum/2))):
        c = (sum - a - b)
        if a**2 + b**2 == c**2:
            sides_of_triangle.append((a, b, c))
    return set(sides_of_triangle)
