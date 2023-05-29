from collections import Counter
def pickingNumbers(a):
    arr = Counter(a)
    maxnum = 0

    for i in range(100):
        maxnum = max(maxnum, arr[i]+arr[i+1])
    return maxnum
