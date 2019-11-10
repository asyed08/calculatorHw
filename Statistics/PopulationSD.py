import math

def population_standard_deviation(a, b, c, d, e, f):
    try:
       a = int(a)
       b = int(b)
       c = int(c)
       d = int(d)
       e = int(e)
       f = int(f)
       xs = [a, b, c, d, e, f]
       mean = sum(xs) / len(xs)
       var = sum(pow(x - mean, 2) for x in xs) / len(xs)
       std = math.sqrt(var)
       return std

    Except ZeroDivisionError:
       print("Cannot divide by zero")
    except ValueError:
        print("Numbers are not valid")