def getSecondOrderElements(n, a):
    # Ensure there are at least two elements in the array
    if n < 2:
        return "Array should have at least two elements"
    
    # Sort the array
    a.sort()

    # Get second highest and second lowest
    second_highest = a[-2]
    second_lowest = a[1]
    
    result = []
    result.append(second_highest)
    result.append(second_lowest)
    
    return result
