def dataStripper(dateModuleResult):
    listOfValues = dateModuleResult.split(",")
    return listOfValues
def dateStriper(daymonth):
    dayMonth = list(daymonth)
    day = int(dayMonth.pop(0))
    m1 = dayMonth.pop(0)
    m2 = dayMonth.pop(0)
    mr = m1+m2
    month = int(mr)
    DayMonth = [day,month]
    return DayMonth