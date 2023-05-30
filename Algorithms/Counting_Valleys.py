def countingValleys(steps, path):
    valleycount = level = 0
    d = {'U':1, 'D':-1}

    for step in path:
        level += d[step]
        if level == 0 and step == 'U':
            valleycount += 1

    return valleycount
