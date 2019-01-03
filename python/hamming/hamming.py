def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Length of strands not equal')
    return sum(i != j for i, j in zip(strand_a, strand_b))
