def countApplesAndOranges(s, t, a, b, apples, oranges):
    totalapples =totaloranges = 0

    for i in range(len(apples)):
        if s <= a + apples[i] <= t:
            totalapples += 1

    for i in range(len(oranges)):
        if s <= b + oranges[i] <= t:
            totaloranges += 1

    print(totalapples)
    print(totaloranges)
