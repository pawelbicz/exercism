DAYS = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
        'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

VERSES = ['a Partridge in a Pear Tree.',
         'two Turtle Doves, ',
         'three French Hens, ',
         'four Calling Birds, ',
         'five Gold Rings, ',
         'six Geese-a-Laying, ',
         'seven Swans-a-Swimming, ',
         'eight Maids-a-Milking, ',
         'nine Ladies Dancing, ',
         'ten Lords-a-Leaping, ',
         'eleven Pipers Piping, ',
         'twelve Drummers Drumming, ']


def __create_sentence(end_verse):
    first_part = f'On the {DAYS[end_verse-1]} day of Christmas my true love gave to me: '
    if end_verse != 1:
        VERSES[0] = 'and a Partridge in a Pear Tree.'
    verses = VERSES[0:end_verse]
    return first_part + ''.join(reversed(verses))


def recite(start_verse, end_verse):
    return [__create_sentence(i) for i in range(start_verse, end_verse+1)]
