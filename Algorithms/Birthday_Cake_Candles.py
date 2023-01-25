def birthdayCakeCandles(candles):
    m = max(candles)
    count = 0
    
    for i in candles:
        if i == m:
            count += 1
    return count
