def miniMaxSum(arr):
    arr.sort()
    sum1 = 0 
    for i in range(0, len(arr)-1):
        sum1 += arr[i]
        
    sum2 = 0
    for i in range(1, len(arr)):
        sum2 += arr[i]
    print(sum1, sum2)
