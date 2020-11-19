# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
# -*- coding: utf-8 -*-

with open('items_list', 'w+', encoding='utf-8') as result_obj:
    while True:
        user_answer = input("Введите данные: ")
        result_obj.write((user_answer + '\n'))
        if user_answer == ' ':
            break
