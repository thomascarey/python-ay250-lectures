
def infseries():
    a = 1
    b = 3
    i = 0
    while i < 100:
        yield a*4
        i += 1
        a -= 1/b
        b += 2
        a += 1/b
        b += 2