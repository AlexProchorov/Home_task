#Очень долго ломал голову с форматом. Понял что D-переводит в десятичное значение, не совсем понял как работет U и I типы десятичный дробей. 

times = int(input("Введите время в секундах:  "))
hours = times // 3600
minutes = (times - hours * 3600) // 60
seconds = times - (hours * 3600 + minutes * 60)

print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))




