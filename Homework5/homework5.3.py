# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('homework5.3.txt','r+',encoding='utf-8') as new_file:
    a = (new_file.readlines())
    print(a)
    print(type(a))
    total=0
    for i in a:
        name, salary, currency = i.split()
        total+=float(salary)
        if float(salary)<20000:
            print(name,salary,currency)
    print('Средняя зарплата по всем  сотрудникам: ', round(total/len(a),2 ))