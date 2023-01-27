def extraLongFactorials(n):
    if n == 0: return 0
    res = 1
    
    while n > 0:
        res *= n
        n -= 1
    return res
