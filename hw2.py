"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


# с адом сложности, как складывать -не понял
from abc import ABC,abstractclassmethod


class Master:
    def __init__(self,param,):
        self.param=param


    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3}'

    @abstractclassmethod
    def con(self):
        return  f'SMTH very abstract'

class Coat(Master):
    def consumption(self):
        return f'Для пошива пальто нужно: {round(self.param / 6.5 + 0.5, 2) } ткани'
    def con(self):
        return 'Second turn'

class Costume(Master):
    def consumption(self):
        return  f'Для пошива костюма надо: {self.param * 2 +0.3} ткани'
    def con(self):
        pass
    def __add__(self, other):
        return f' Суммарно для пошива {self.param() + other.param()}'
coat=Coat(4505)
costume= Costume(70)
print(coat.consumption())
print(costume.consumption())
print()