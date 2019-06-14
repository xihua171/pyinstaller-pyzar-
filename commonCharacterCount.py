def commonCharacterCount(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    z = 0
    for i3 in s1:
        if i3 in s2:
            z = z+1
            s2.remove(i3)
    return (z)
