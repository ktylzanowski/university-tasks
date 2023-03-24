import math


def div_sum(x, y):
    list_of = {}

    if x > y:
        y, x = x, y

    if y < 284:
        return {}

    if x < 220:
        x = 220

    for j in range(x, y):
        result = 0
        for i in range(2, int(math.sqrt(j)+1)):
            if j % i == 0:
                if i == (j / i):
                    result += i
                else:
                    result += i + j / i
        list_of[j] = int(result+1)
    return check_for_friendly(list_of)


def check_for_friendly(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        try:
            if key == dictionary[value] and key != value:
                if value not in new_dict:
                    new_dict[key] = value
        except KeyError:
            pass
    return new_dict
