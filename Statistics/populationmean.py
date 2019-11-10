from Calculator.addition import addition
from Calculator.division import division
from pprint import pprint
def popmean(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        data = []
        data.append(a)
        data.append(b)
        data.append(c)
        total_n = len(data)
        sum = 0
        for i in data:
            sum = addition(sum,i)
        mean = division(sum,total_n)
        pprint(mean)
        return mean
    except ZeroDivisionError:
        print("Divide by Zero Error")
    except ValueError:
        print("Only float arguments are valid.")