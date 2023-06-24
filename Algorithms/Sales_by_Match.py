def sockMerchant(n, ar):
    table = {}
    count = 0

    for ele in ar:
        if ele in table:
            count += 1
            table.pop(ele)

        else:
            table[ele] = 1
    return count
