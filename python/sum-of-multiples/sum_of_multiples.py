def sum_of_multiples(limit, multiples):
    return sum(set(x
                   for multiple in multiples if multiple > 0
                   for x in range(multiple, limit, multiple)
                   ))

