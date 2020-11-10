
goods=[]

while True:
    user_wishes= input('Хотите ли Вы добавить новый продукт? Выберите: "y" или "n". Ваш ответ: ')
    if user_wishes == 'y':
        number=int(input('Введите порядковый номер позиции товара: '))
        featurs={}
    else:
        print('Информация принята')
        break
    while True:
        user_corret = input('Хотите ли Вы добавить параметры товара? Выберите: "Y" или "N". Ваш ответ: ')
        if user_corret == 'y':
            featurs_key=input('Введите наименовании позиции: ')
            featurs_value=input('Введите ценовую характеристику позиции: ')
            featurs[featurs_key]=featurs_value
            goods.append(tuple([number,featurs]))
            break
        else:
            print('Информация принята')
            break
print((goods))

analitics = {}
for good in goods:
    for featurs_key, featurs_value in good[1].items():
        if featurs_key in analitics:
            analitics[featurs_key].append(featurs_value)
        else:
         analitics[featurs_key] = [featurs_value]
print(analitics)

