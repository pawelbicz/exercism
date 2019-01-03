import string as s


def is_pangram(sentence):

    text = remove_punctuation(sentence)
    dictionary = create_dictionary()
    dictionary = assert_letters_in_sentence(text, dictionary)
    return verify_dictionary(dictionary)


def remove_punctuation(text):
    result = ''
    for i in text:
        if i not in s.punctuation:
            result += i
    return result


def create_dictionary():
    d = {}
    for i in s.ascii_lowercase:
        d[i] = False
    return d


def assert_letters_in_sentence(text, d):
    for i in text.lower():
        d[i] = True
    return d


def verify_dictionary(d):
    for i in d:
        if d[i] is False:
            return False
    return True
