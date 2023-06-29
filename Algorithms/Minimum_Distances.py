def minimumDistances(a):
    distance = sys.maxsize

    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                distance = min(distance, j - i)

    if distance == sys.maxsize:
        return -1
    else:
        return distance
