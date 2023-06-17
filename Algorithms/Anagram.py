from collections import Counter

def anagram(s):
    n = len(s)

    if n % 2 == 1:
        return -1

    s = Counter(s[:n//2]) - Counter(s[n//2:])
    return sum(s.values())
