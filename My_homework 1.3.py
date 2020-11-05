# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_answer=input("Сударь, введите любое число: ")

nubmer2 = user_answer + user_answer
number3 = nubmer2 + user_answer
print(nubmer2, number3)

summ = int(user_answer) + int(nubmer2) + int(number3)
print (summ)