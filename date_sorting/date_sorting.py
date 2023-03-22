import datetime


def bubblesort(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i]['year'] > elements[i + 1]['year']:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
            elif elements[i]['year'] == elements[i + 1]['year'] and elements[i]['month'] > elements[i + 1]['month']:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
            elif elements[i]['year'] == elements[i + 1]['year'] and elements[i]['month'] == elements[i + 1]['month'] \
                    and elements[i]['day'] > elements[i + 1]['day']:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
    return elements


def date_into_dict(dates):
    dict_of_days = {}
    for i in range(len(dates)):
        date = datetime.datetime.strptime(dates[i], '%d/%m/%Y').date()
        dict_of_days[i] = {'day': date.day, 'month': date.month, 'year': date.year}
    return bubblesort(dict_of_days)

