 def saveThePrisoner(n, m, s):
    if((m+s-1)%n == 0):
        return n
        
    else:
        return (m+s-1)%n
