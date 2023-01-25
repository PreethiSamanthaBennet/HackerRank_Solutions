def plusMinus(arr):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    
    for i in range(0, len(arr)):
        if arr[i] > 0:
            sum1 += 1
            
        elif arr[i] < 0:
            sum2 += 1
            
        else:
            sum3 += 1
            
    print(round(sum1/len(arr), 6))
    print(round(sum2/len(arr), 6))
    print(round(sum3/len(arr), 6))
