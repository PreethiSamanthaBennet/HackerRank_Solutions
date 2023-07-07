import calendar

mdy = input()

mdy = mdy.split()

mm = int(mdy[0])
dd = int(mdy[1])
yyyy = int(mdy[2])

c = calendar.weekday( yyyy, mm, dd)

if c == 0:
    print("MONDAY")

if c == 1:
    print("TUESDAY")

if c == 2:
    print("WEDNESDAY")

if c == 3:
    print("THURSDAY")

if c == 4:
    print("FRIDAY")

if c == 5:
    print("SATURDAY")

if c == 6:
    print("SUNDAY")
