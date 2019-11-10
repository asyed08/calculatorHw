

def mode(a, b, c, d, e):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        data = []
        data.append(a)
        data.append(b)
        data.append(c)
        data.append(d)
        data.append(e)
        count = 0
        for i in data:
            for j in data:
                if(j == i):
                    count = count + 1
                if
    except ValueError:
        print("No values with multiple frequencies")
