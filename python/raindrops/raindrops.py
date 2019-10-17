def convert(number):
    raindrops = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))
    sound = [s for n, s in raindrops if number % n == 0]
    return ''.join(sound) if sound else str(number)
