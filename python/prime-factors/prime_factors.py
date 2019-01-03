def prime_factors(number):
    """Return list of a prime numbers which multiplication gives 'number'"""
    l_factor = []
    n = 2
    while number > 1:
        if number % n == 0:
            l_factor.append(n)
            number /= n
            n = 1
        n += 1
    return l_factor
