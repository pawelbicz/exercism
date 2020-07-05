import re
from collections import Counter


def count_words(sentence):
    clean_sentence = re.sub(r"[:!@#\$%\^&,\._]| '|' |''|^'|'$", ' ', sentence.lower())
    return Counter(clean_sentence.split())

