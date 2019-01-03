def largest_product(series, size):
    if size < 0:
        raise ValueError('Input incorrect')
    return max(calc(series, size, i) for i in range(len(series) - size + 1))


def calc(k, s, i):
    val = 1
    for n in range(s):
        val *= int(k[i + n])
    return val
