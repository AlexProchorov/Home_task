user_str=input('Введите любые слова: ').split()



for indx, words in enumerate(user_str,1):
    if len(words) > 10:
        print(indx,words[:10])
    else:
        print(indx, words)