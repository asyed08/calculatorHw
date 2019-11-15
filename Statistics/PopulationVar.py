from Statistics.PopulationSD import population_standard_deviation
from Calculator.square import square

def population_variance(a, b, c, d, e, f):
    try:
        popstd = population_standard_deviation(a,b,c,d,e,f)
        answer = square(popstd)
        return answer
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Numbers are not valid")
