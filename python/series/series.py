def slices(series, length):
    if len(series) < length or length < 1:
        raise ValueError('Length value incorrect')
    num_of_slices = len(series) - (length-1)
    return[series[i:length+i] for i in range(num_of_slices)]
