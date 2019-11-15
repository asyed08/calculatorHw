from Calculator.addition import addition
from Calculator.square import square
from Calculator.squareroot import squareroot

def population_standard_deviation(a, b, c, d, e, f):
    try:
       a = int(a)
       b = int(b)
       c = int(c)
       d = int(d)
       e = int(e)
       f = int(f)
       xs = [a, b, c, d, e, f]
       a1 = addition(a,b)
       b2 = addition(a1,c)
       c3 = addition(b2,d)
       d4 = addition(c3,e)
       sum = addition(d4,f)

       mean = sum/(len(xs))
       sum1 = 0
       for i in xs:
            curr = float(i - mean)
            z = square(curr)
            sum1 = sum1 + z
       num1 = sum1/(len(xs))
       answer = float(squareroot(num1))
       return answer
    except ZeroDivisionError:
       print("Cannot divide by zero")
    except ValueError:
        print("Numbers are not valid")