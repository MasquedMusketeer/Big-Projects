month28 = [2]
month30 = [4,6,9,11]

def dayMonthEncoder (daymonth):
    setStart = daymonth.pop(0)
    month = daymonth.pop(0)
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
            setStart += 1
        if setStart > 7:
            setStart = 1
#day to be recorded for next month calculation:
    nextMonth = month + 1
    if nextMonth > 12:
        nextMonth = 1
    if nextMonth > 9:
        nextDayMonth = str(setStart) + str(nextMonth)
    else:
        nextDayMonth = str(setStart) + ("0" + str(nextMonth))

#returning result:
    result = [fullDay, HalfDay, int(nextDayMonth)]
    return result
