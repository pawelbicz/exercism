def is_isogram(string):
    string = ''.join([i.lower()  for i in string if i.isalpha()])
    for char in string:
        if string.count(char) > 1:
            return False
    return True
