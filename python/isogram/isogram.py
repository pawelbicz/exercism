def is_isogram(string):
    word = ''.join([char.lower() for char in string if char.isalpha()])
    single_letters = []
    [single_letters.append(char) for char in word if word.count(char) == 1]

    return len(word) == len(single_letters)