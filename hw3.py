"""Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (
__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно
осуществляться округление значения до целого числа.
- Сложение. Объединение двух клеток. При этом число ячеек общей
клетки должно равняться сумме ячеек исходных двух клеток.
- Вычитание. Участвуют две клетки. Операцию необходимо
выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
- Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
этих двух клеток.
- Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку
вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование
ряда не хватает, то в последний ряд записываются все оставшиеся."""


class Cletka:
    def __init__(self,count):
        self.count = count
    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        sub = self.count-other.count
        if sub >0:
            return  sub
        else:
            print(f'Разница отрицательна')
        return ' '

    def __mul__(self, other):
        return  self.count * other.count

    def __truediv__(self, other):
        return  round(self.count / other.count, 0)

    def make_order(self,row):
        result = ''
        for i in range(int(self.count/row)):
            result += '*' * row+ '\n'
        result+= '*' * (self.count % row) + '\n'
        return result

y=Cletka(200)
y_2=Cletka(354)
print(y / y_2)
print(y * y_2)
print( y + y_2)
print( y - y_2)
print(y.make_order(55))