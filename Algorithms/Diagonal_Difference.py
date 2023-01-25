def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    
    for i in range(0, len(arr)):
        sum1 += arr[i][i]
        
    for i in range(0, len(arr)):
        sum2 += arr[i][len(arr)-1-i]

    if sum1 >= sum2:
        return sum1 - sum2

    else:
        return sum2 - sum1
