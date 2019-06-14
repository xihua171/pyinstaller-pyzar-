def isLucky(n):
    n = str(n)
    a = 0
    b = 0
    for i in (n[0:int(len(n)/2)]):
        a = a+int(i)    
    for i2 in (n[int(len(n)/2):int(len(n))]):
        b = b+int(i2)
    if a == b:
        return True
    else:
        return False

