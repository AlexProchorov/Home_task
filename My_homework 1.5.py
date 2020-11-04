import math

money_plus=int(input('Введите значение выручки фирмы: '))
money_minus=int(input('Введите значения издержек фирмы: '))

if money_plus > money_minus:
    print('Вы хороший бизнесмен. Есть прибыль! ')
    rent=money_plus/money_minus
    print(f'Рентабельность фирмы составляет: {round(rent, 3)}')
    count=int(input('Введите количество сотрудников на предприятии: '))
    count_major= (money_plus-money_minus)/count
    print(f'В расчете на 1 сотрудника прибыль составляет {round(count_major,2)} рублей')
else:
    print('Что то пошло не так. Расходы слишком большие.')