def compareTriplets(a, b):
    array = []
    x = 0
    y = 0

    for i in range(0, len(a)):
        if a[i] > b[i]:
            x += 1
        elif a[i] < b[i]:
            y += 1
        else:
            continue
            
    array.append(x)
    array.append(y)
    return array
