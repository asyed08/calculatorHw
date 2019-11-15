def median(a, b, c, d, e, f, g):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        f = int(f)
        g = int(g)
        data = [a, b, c, d, e, f, g]
        num = len(data)
        sort = sorted(data)
        function = (sum(sort[num // 2 - 1:num // 2 + 1]) / 2.0, sort[num // 2])[num % 2] if num else None
        return function
    except ZeroDivisionError:
        print("Not a valid number")
    except ValueError:
        print("Only numerical values")