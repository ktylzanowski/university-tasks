import math


def divSum(x, y):
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
                    result = result + i
                else:
                    result = result + (i + j / i)
        list_of[j] = int(result+1)
    return check_for_friendly(list_of)


def check_for_friendly(dict):
    new_dict = {}
    for key, value in dict.items():
        try:
            if key == dict[value] and key != value:
                if value in new_dict:
                    continue
                new_dict[key] = value
        except KeyError:
            pass
    return new_dict