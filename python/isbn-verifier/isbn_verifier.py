import re


def is_valid(isbn):
    """    Return True if isbn formulea modulo 11 == 0    """
    isbn_parsed = re.findall(r'\d|X$', isbn)
    if len(isbn_parsed) == 10:
        if isbn_parsed[-1] == 'X':
            isbn_parsed[-1] = '10'
        return compute_isbn_formulea(isbn_parsed) % 11 == 0
    return False


def compute_isbn_formulea(isbn):
    """    Return result of isbn formulea    """
    return sum(int(val) * i for val, i in zip(isbn, range(10, 0, -1)))
