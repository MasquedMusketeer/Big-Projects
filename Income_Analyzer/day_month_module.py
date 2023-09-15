month28 = [2]
month30 = [4,6,9,11]

def dayMonthEncoder (day, month):
    setStart = day
    dayCounter = 0
    fullDay = 0
    HalfDay = 0
#setting how many loops will be made:
    if month in month28:
        dayCounter = 28
    elif month in month30:
        dayCounter = 30
    else:
        dayCounter = 31
#loop:
    while dayCounter > 0:
        if setStart == 1 or setStart == 2 or setStart == 3:
            fullDay += 1
            setStart += 1
            dayCounter -= 1
        elif setStart == 4 or setStart == 5:
            HalfDay += 1
            setStart += 1
            dayCounter -= 1
        else:
            dayCounter -= 1
        if setStart > 7:
            setStart = 1
#returning result:
    return fullDay, HalfDay
