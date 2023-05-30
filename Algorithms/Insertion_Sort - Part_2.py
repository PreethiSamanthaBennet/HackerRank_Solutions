def insertionSort2(n, arr):
    for j in range(1, n):
        key = arr[j]
        i = j

        while i > 0 and arr[i-1] > key:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = key
        print(*arr)
