from Calculator.addition import addition
from Calculator.division import division

def mean(data):
    total_n = len(data)
    sum = 0
    for i in data:
        sum = addition(sum,i)
    mean = 0
    mean = division(sum,total_n)
    return mean