# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import sys
def result():
    new_argv = int(argv[0]) * int(argv[1]) + int(argv[2])
    return new_argv
argv=sys.argv[1:]

if 'h' in argv or 'help' in argv:
    print('Как работает программа: \nСначала осуществляется ввода отработанных часов. Следующим шагом - оплата в час, в конце - премия')
if len(argv) >= 2:
    print('Выработка в часах:', argv[0])
    print('Оплата в час:', argv[1])
    print('Премия: ',argv[2])
    print(result())
