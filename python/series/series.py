def slices(series, length):
    if len(series) < length:
        raise ValueError('Length of series to small')
    if length < 1:
        raise ValueError("Length can't be smaller than 1")
    num_of_slices = len(series) - (length - 1)
    return[series[0+i:length+i] for i in range(num_of_slices)]
