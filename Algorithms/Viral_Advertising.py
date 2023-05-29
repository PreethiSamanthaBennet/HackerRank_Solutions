def viralAdvertising(n):
    total_likes = 0
    shared = 5

    for i in range(n):
        like = shared//2
        total_likes += like
        shared = like*3

    return total_likes
