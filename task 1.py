def func(a):
    if a <0 or a > 1000:
        return 0
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        return True
    else:
        return False
print(func(int(input())))