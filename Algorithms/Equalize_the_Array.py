from collections import Counter

def equalizeArray(arr):
    c = Counter(arr)
    return len(arr) - max(c.values())
