def migratoryBirds(arr):
    l = [0] * len(arr)

    for i in range(len(arr)):
        l[arr[i]] += 1

    return l.index(max(l))
