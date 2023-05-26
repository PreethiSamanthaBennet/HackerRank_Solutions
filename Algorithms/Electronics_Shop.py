def getMoneySpent(keyboards, drives, b):
    maxamount = -1
    for keyboard in keyboards:
        for drive in drives:
            if keyboard+drive <= b:
                maxamount = max(maxamount, keyboard+drive)
    return maxamount
