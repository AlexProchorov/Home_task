first_result=int(input("Введите результат первого дня пробежки в КМ: "))
aim_result=int(input("Введите желаемый результат в КМ: "))

day = 0

while first_result < aim_result:
    first_result = first_result * 1.1
    day += 1
print(day)
