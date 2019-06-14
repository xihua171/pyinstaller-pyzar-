def allLongestStrings(inputArray):
    x = []
    for i in inputArray:
        x.append(len(i))
    y = []
    for i2 in inputArray:
        if len(i2) == max(x):
            y.append(i2)
    return (y)
