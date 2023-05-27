def repeatedString(s, n):
    total = 0
    
    for i in s:
        if i == 'a':
            total += 1

    total = n//len(s)*total

    for i in s[:n%len(s)]:
        if i == 'a':
            total += 1

    return total
