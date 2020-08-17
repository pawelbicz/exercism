LETTER_VALUE = {'aeioulnrst': 1,
                'dg': 2,
                'bcmp': 3,
                'fhvwy': 4,
                'k': 5,
                'jx': 8,
                'qz': 10}
LETTERS_TO_SCORE = dict((k, v) for i, v in LETTER_VALUE.items() for k in str(i))


def score(word):
    return sum(LETTERS_TO_SCORE[i] for i in word.lower())
