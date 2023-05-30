def quickSort(arr):
    left = []
    right = []
    pivot = arr[0]

    i = 0
    j = len(arr)-1

    while i < j:
        while i < j and arr[i] <= pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    arr[0], arr[j] = arr[j], arr[0]
    return arr
