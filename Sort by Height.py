def sortByHeight(a):
    x = []
    y = []
    for i in range(len(a)):
        if a[i] == -1:
            x.append(i)
        else:
            y.append(a[i]) 
    a = (sorted(y))
    for i2 in x:
        a.insert(i2,-1)
    return (a)
