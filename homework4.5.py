#  Реализовать формирование списка, используя функцию range() и возможности генератора.
#  В список должны войти четные числа от 100 до 1000 (включая границы).
#  Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def new_fucn(one,two):
    return one * two



new_result= [ el for el in range(100,1000) if el % 2 == 0 ]
print(new_result)
endlist = reduce(new_fucn, new_result)
print (endlist)