import string


def is_pangram(phrase):
    phrase_wo_punctuation = ''.join(x for x in phrase.replace(' ', '') if x not in string.punctuation)
    return set(phrase_wo_punctuation.lower()) >= set(string.ascii_lowercase)
