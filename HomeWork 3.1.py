def new_func(a,b):
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        result= a // b
        return result

a = int(input("Введите число"))
b = int(input("Введите число 2"))

print(new_func(a,b))
