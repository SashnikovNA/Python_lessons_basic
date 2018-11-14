# Сашников Никита


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

#Создаем класс "Треугольничег"
class Triangle:

# указываем атрибуты через инит
    def __init__(self, point_XA, point_YA, point_XB, point_YB, point_XC, point_YC):
        self.point_XA = point_XA
        self.point_YA = point_YA
        self.point_XB = point_XB
        self.point_YB = point_YB
        self.point_XC = point_XC
        self.point_YC = point_YC


# прогуливаемся по методам, они же функции в прошлом :-)

# тут определяем длины сторон
# Применим теорему Пифагора: |AB|² = (y2 - y1)² + (x2 - x1)².
    def len_triangle(self):
        a = lambda a_1, a_2: (a_1 - a_2) ** 2
        self.len_AB = math.sqrt(a(self.point_XA, self.point_XB) + a(self.point_YA, self.point_YB))
        self.len_AC = math.sqrt(a(self.point_XA, self.point_XC) + a(self.point_YA, self.point_YC))
        self.len_BC = math.sqrt(a(self.point_XB, self.point_XC) + a(self.point_YB, self.point_YC))


# Далее по формулам - высота, площадь, периметр

    def height_triangle(self):
        p = (self.len_BC + self.len_AB + self.len_AC) * 0.5
        a_base = lambda p, x: p - x
        self.height = (((p * a_base(p, self.len_AB) * a_base(p, self.len_AC) * a_base(p, self.len_BC)) ** 0.5) * 2) / self.len_BC

    def area_triangle(self):
        self.area = (self.height * self.len_BC) * 0.5

    def perimeter_triangle(self):
        self.perimeter = self.len_BC + self.len_AC + self.len_AB


# и вот он наш родимый - объект в виде коров треуголки
real_triang = Triangle(1, 1, 15, 1, 12, 15)

# прогуливаемся по методам для объекта
real_triang.len_triangle()
real_triang.height_triangle()
real_triang.area_triangle()
real_triang.perimeter_triangle()

print("Задание 1")
# Допом в принтах округление дробной части до сотых
print("Площадь треугольника: ", '%.2f' % real_triang.area)
print("Высота треугольника: ", '%.2f' % real_triang.height)
print("Периметр треуголика: ", '%.2f' % real_triang.perimeter)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

print("Задача 2")
import math


#Во второй задаче пробую использовать родительский класс и поглядеть на наследование
# + упростить атрибуты, точнее их кол-во на входе (теперь это не каждая отдельная точка, а группы координат)

#
class figure:
    def __init__(self):
        pass
    def storona(self,t1,t2):
        return math.sqrt((int(t1[0])- int(t2[0]))**2 + (int(t1[1]) - int(t2[1]))**2)


class Trapec(figure):
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.AB = self.storona(self.A, self.B)
        self.BC = self.storona(self.B, self.C)
        self.CD = self.storona(self.C, self.D)
        self.AD = self.storona(self.A, self.D)

    # @property - позволяет обращаться к методу как к атрибуту
    # Если я правильно понял, то это позволяет без призыва метода для объекта сразу пулять его в принт, как атрибут :)

    @property
    def isravnob(self):
        if self.storona(self.A, self.C) == self.storona(self.B, self.D):
            return True
        else:
            return False

    @property
    def Ploschad(self):
        if self.isravnob:
            S = ((self.BC + self.AD) / 2) * math.sqrt(self.AB ** 2 - ((self.BC - self.AD) ** 2) / 4)
            return S
        else:
            print('Трапеция не равнобедренная')
            return 0

    @property
    def Perimetr(self):
        return self.AB + self.BC + self.CD + self.AD


real_trap = Trapec((1, 1), (2, 6), (5, 6), (6, 1))
if real_trap.isravnob:
    print('Трапеция равнобедренная')
else:
    print('Трапеция НЕ равнобедренная')
print('Периметр трапеции: ', str( '%.2f' % real_trap.Perimetr))
print('Площадь трапеции: ', str( '%.2f' % real_trap.Ploschad))
