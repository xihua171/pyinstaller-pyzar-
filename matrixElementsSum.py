def matrixElementsSum(matrix):
    x = []
    for i in matrix:
        a = len(i)
        for i2 in i:
            x.append(i2)
    print (x)
    for i3 in range(len(x)):
        if x[i3] == 0:
            try:
                x[i3+a] = 0
            except:
                pass

    return sum(x)  
