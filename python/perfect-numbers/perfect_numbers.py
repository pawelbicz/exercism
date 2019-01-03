def classify(number):
    l_num = []
    [l_num.append(i+1) for i in range(number) if number % (i+1) == 0]
    l_num.remove(number)
    if sum(l_num) == number:
        return "perfect"
    elif sum(l_num) > number:
        return "abundant"
    else:
        return "deficient"
