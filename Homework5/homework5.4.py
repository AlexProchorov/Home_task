# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open ('homework5.4.txt',encoding='utf-8') as new_file:
    obj=new_file.readlines()
    print(obj)
    new_dict={
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
    }
with open ('homework5.4.new.txt','w',encoding='utf-8') as data_write:
    for i in obj:
        line=i.split()
        line[0]=new_dict[line[0]]
        data_write.write((''.join(line) + '\n'))