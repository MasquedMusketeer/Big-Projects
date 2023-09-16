unusedValues = []

def dateStripper(dateModuleResult):
    listOfValues = dateModuleResult
    fullDay = listOfValues.pop(0)
    halfDay = listOfValues.pop(0)
    nextMonthValue = listOfValues.pop(0)
    unusedValues.append(nextMonthValue)
    result = [halfDay, fullDay]
    
    return result
    
