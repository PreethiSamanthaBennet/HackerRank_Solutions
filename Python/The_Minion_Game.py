def minion_game(string):
    s = len(string)
    con, vow = 0, 0

    for i in range(s):
        if string[i] in 'AEIOU':
            vow += (s - i)

        else
            con += (s - i)

    if con>vow:
        print('Stuart {}' .format(con))

    elif con == vow:
        print('Draw')

    else:
        print('Kevin {}' .format(vow))
