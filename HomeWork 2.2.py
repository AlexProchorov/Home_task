
my_list = input ("Введите любые цифры через пробел").split()

new_list = ()

for i in range(1, len(my_list), 2):
    my_list [i - 1], my_list [i] = my_list[i], my_list[i - 1]
print(''.join([str(i) for i in my_list]))







