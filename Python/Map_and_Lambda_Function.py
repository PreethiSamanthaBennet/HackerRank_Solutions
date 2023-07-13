def fibonacci(n):
    a = 0
    b = 1
    l = []

    if n == 0:
        pass

    elif n == 1:
        l.append(a)

    else:
        l.append(a)    
        l.append(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            l.append(c)

    return l

cube = lambda x : x ** 3
