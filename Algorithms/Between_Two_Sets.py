from functools import reduce

def getTotalX(a, b):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a%b)
        
    def lcm(a, b):
        return a*b//gcd(a, b)
        
    g = reduce(gcd, b)
    l = reduce(lcm, a)

    s = 0
    
    for i in range(l, g+1, l):
        if g%i == 0:
            s += 1
    return s
