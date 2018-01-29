
import math

def infseries():
    a = 1
    b = 3
    dif = 1
    lim = 0.1*math.pi
    while dif > lim:
        yield a*4
        dif = abs(math.pi-a)
        a -= 1/b
        b += 2
        a += 1/b
        b += 2