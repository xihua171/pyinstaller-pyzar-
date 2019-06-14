def makeArrayConsecutive2(statues):
    x = []
    for i in range(min(statues),max(statues)):
        x.append(i)
    return len(x)-len(statues)+1
