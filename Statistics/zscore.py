from Statistics.PopulationSD import population_standard_deviation

def zscore(datapoint, a, b, c, d, e, f):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
        f = float(f)
        data = []
        data.append(a)
        data.append(b)
        data.append(c)
        data.append(d)
        data.append(e)
        data.append(f)
        sum = a+b+c+d+e+f
        mean = sum/len(data)
        sd = population_standard_deviation(a,b,c,d,e,f)
        result = (datapoint-mean)/sd
        return result
    except ZeroDivisionError:
       print("Cannot divide by zero")
    except ValueError:
        print("Numbers are not valid")
