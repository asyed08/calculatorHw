from Statistics.PopulationSD import population_standard_deviation

def sample_standard_deviation(samplesize,a,b,c,d,e,f,g,h):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
        f = float(f)
        g = float(g)
        h = float(h)
        samplesize = int(samplesize)
        data = []
        data.append(a)
        data.append(b)
        data.append(c)
        data.append(d)
        data.append(e)
        data.append(f)
        data.append(g)
        data.append(h)
        sample = []
        for i in range(1,samplesize):
            sample.append(int(data[i]))
        return population_standard_deviation(sample[1],sample[2],sample[3],sample[4],sample[5],sample[6])
    except ZeroDivisionError:
       print("Cannot divide by zero")
    except ValueError:
        print("Numbers are not valid")