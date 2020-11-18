def amazing_fucn(x,y):
    result = x ** y
    return result

print((amazing_fucn(1,-2)))


def hard_func(x,y):
    result = 1
    for i in range(abs(y)):
       result *= x
    if y<0:
        return 1/result
    return result

print(hard_func(2,3))
