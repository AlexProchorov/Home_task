# Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('homework5.2.txt', 'r',encoding='utf-8') as homework522:
    result_lines=homework522.readlines()
    print(f' Количество строк равно: {len(result_lines)}') #первый способ


    f = open('homework5.2.txt')
    line=0
    for i in f:
        line +=1
        flag=0
        word=0
        for j in  i:
            if j != ' ' and flag == 0:
                word+=1
                flag = 1
            elif j == ' ':
                flag = 0
        print( i, len(i), ' симв.', word, 'сл.')
    print(line, 'стр')
    f.close()

