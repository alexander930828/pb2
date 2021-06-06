def atleast_n(a):
    n = len(a)
    low_n = a[0]
    for i in range(n):
        if a[i] < low_n:
            low_n = a[i]
    return low_n

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(atleast_n(v))