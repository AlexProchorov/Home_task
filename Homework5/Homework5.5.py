# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random
user_count=int(input('Введите количество чисел: '))


with open ('HOMEWORK5.5.txt', 'w+',encoding='utf-8') as new_file:
    for i in range(user_count):
        new_file.write(f' {random.randint(1,100)}'+'\n')
    new_file.seek(0)
    ls_sum=new_file.readline().split()
    print(ls_sum)
result=sum(map(int,ls_sum))
print(f'Сумма числен из рандома равна: {result}')
