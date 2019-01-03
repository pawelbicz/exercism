import re


def hey(phrase):
    phrase = re.sub('\s', '', phrase)
    if not phrase:
        return "Fine. Be that way!"
    elif phrase.isupper():
        return "Whoa, chill out!"
    elif phrase.endswith('?'):
        return "Calm down, I know what I'm doing!" if phrase.isupper() else "Sure."
    else:
        return "Whatever."
