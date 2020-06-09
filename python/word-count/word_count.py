import re

def count_words(sentence):
    words = {}
    sen = sentence.lower()
    for word in re.split(r"\W|_", sen,):
        if word not in words:
           words[word] = 1
        elif word in words:
            words[word] += 1
    if '' in words:
        del words['']
    return words
