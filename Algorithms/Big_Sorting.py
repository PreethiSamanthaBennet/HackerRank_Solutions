def bigSorting(unsorted):
    unsorted.sort(key = lambda x : (len(x), x))

    return unsorted
