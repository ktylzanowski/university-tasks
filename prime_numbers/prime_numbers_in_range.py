def prime_numbers(lower, upper):
    if lower > upper:
        lower, upper = upper, lower

    list_of_numbers = []
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                list_of_numbers.append(num)
    return list_of_numbers if len(list_of_numbers) > 0 else False
