def score(word):
    letters_value = dict(aeioulnrst=1, dg=2, bcmp=3, fhvwy=4, k=5, jx=8, qz=10)
    letter_value = [(i, v) for k, v in letters_value.items() for i in str(k)]
    return sum([dict(letter_value)[i] for i in word.lower()])

