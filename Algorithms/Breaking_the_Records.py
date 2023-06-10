def breakingRecords(scores):
    mincount = maxcount = 0
    minscore = maxscore = scores[0]

    for i in range(1, len(scores)):
        if minscore < scores[i]:
            minscore = scores[i]
            mincount += 1

        elif maxscore > scores[i]:
            maxscore = scores[i]
            maxcount += 1

    return mincount, maxcount
