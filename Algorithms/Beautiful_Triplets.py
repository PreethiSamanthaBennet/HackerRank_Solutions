def beautifulTriplets(d, arr):

    m = Counter(arr)
    count = 0

    for num in arr:
        if m[num + d] and m[num + d + d]:
            count += 1
    return count
