#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

user_answer = int(input("Введите любое целое число"))

m = user_answer % 10

while user_answer > 0:
    if user_answer % 10 > m:
        m = user_answer % 10
    user_answer = user_answer//10
print(m)

