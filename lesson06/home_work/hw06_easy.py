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

