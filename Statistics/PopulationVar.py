

def population_variance(a, b, c, d, e, f):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        f = int(f)
        sample = [a, b, c, d, e, f]
        m = sum(sample) / len(sample)
        pop_var = sum((xi - m) ** 2 for xi in sample) / len(sample)
        return pop_var

    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Numbers are not valid")
