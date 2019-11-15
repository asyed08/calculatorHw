from statistics import StatisticsError

from Statistics.UtilityMethods import numbers


def mode(data):
    try:
        numbers(data)
        num_count = [data.count(a) for a in data]
        x = [data[i] for i, value in enumerate(num_count) if value == max(num_count)]
        x = list(set(x))
        if len(x) == len(data):
            return None
        elif len(x) == 1:
            return x[0]
        else:
            return x
    except StatisticsError:
        print("No values with multiple frequencies")
