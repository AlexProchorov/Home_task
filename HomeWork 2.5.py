my_list = [7, 5, 3, 3, 2,9]

user_answer=int(input('Введите число рейтинг-таблицы: '))
my_list.append((user_answer))
my_list.sort(reverse=True)
print(my_list)
