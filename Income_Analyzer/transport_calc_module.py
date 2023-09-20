def totalValueCalculator(damomResult):
    halfDay = damomResult.pop(0)
    fullDay = damomResult.pop(0)
    totalUnitsHalfEntry = halfDay + 2 * fullDay
    totalUnitsFullEntry = halfDay + fullDay
    totalHalfDay = totalUnitsHalfEntry * 2.2
    totalFullDay = totalUnitsFullEntry * 4.4
    totalOfMonth = totalHalfDay + totalFullDay

    result = [round(totalOfMonth, 2), round(totalHalfDay, 2), round(totalFullDay, 2)]
    return result