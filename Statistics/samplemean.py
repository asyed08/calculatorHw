from Calculator.addition import addition
from Calculator.division import division
import random

def sampmean(samplesize, a ,b, c, d, e):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
        data = []
        data.append(a)
        data.append(b)
        data.append(c)
        data.append(d)
        data.append(e)
        sample = random.sample(data,samplesize)
        total_n = len(sample)
        sum = 0
        for i in sample:
            sum = addition(sum,i)
        mean = division(total_n,sum)
        return mean
    except ZeroDivisionError:
        print("Divide by Zero Error")
    except ValueError:
        print("Only float arguments are valid.")
