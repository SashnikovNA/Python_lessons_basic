#!/usr/bin/python3

# Выполнил - Сашников Никита
"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random

#а создадим-ка кучу функций под всё это дело :-)

# Определяем какие значения будут попадать в карточки игроков:
def lot():
    lot = set()
    while len(lot) < 15:
        y = random.randint(1, 90)
        lot.add(y)
    lot = list(lot)
    return lot

# функция формирования удобоваримого представления строк
# карточек в окне терминала
def space_ins(lot, lot_begin, lot_end):
    a = sorted(lot[lot_begin:lot_end])
    y = 0
    while y != 4:
        x = random.randint(0, len(lot))
        a.insert(x, ' ')
        y += 1
    return a

# Функция генерации последовательности выпадания цифр на бочонке
def random_sample():
    x = []
    sample = list(range(1, 91))
    random.shuffle(sample)
    for number in sample:
        x.append(number)
    return x

game = int(random.randint(1, 91))

# функция поиска совпадений числа на бочонке с числами в карточках
def find_numb_bo4ka(number, a):
    for x in a:
        if x == number:
            z = a.index(x)
            x = '-'
            a[z] = x
    return a




# Функция вывода полной карточки (название + цифры карты)
def print_information(x, a, b, c):
    print("\n", '*' * 10, x, '*' * 10)
    print(a)
    print(b)
    print(c)
    print('*' * 35, "\n")


# Поехали уже наконец - то программу писать

# Создаем 2 карточки для себя и любимого робота
lot_1 = lot()
lot_2 = lot()


# формируем карточку игрока
a = space_ins(lot_1, 0, 5)
b = space_ins(lot_1, 5, 10)
c = space_ins(lot_1, 10, 15)

# формируем карточку компьютера
d = space_ins(lot_2, 0, 5)
e = space_ins(lot_2, 5, 10)
f = space_ins(lot_2, 10, 15)

# бочка даёт показания
u = random_sample()

# необходимые счетчики для человека и машины
cycle = 0
true_hum = 0
true_com = 0
victory_hum = 0
victory_com = 0

# Основная реализация - циклы и сравнения
while cycle < 90:
    for v in a + b + c:
        v = str(v)
        if v.isdigit():
            true_hum += 1
    for v in d + e + f:
        v = str(v)
        if v.isdigit():
            true_com += 1
    if victory_hum < true_hum and victory_com < true_com:
        victory_hum = true_hum
        victory_com = true_com
        number = u[cycle]
        print(' Бочонок показывает нам цифру ', number)
        print_information('Моя карточка', a, b, c)
        print_information('Карта ИИ', d, e, f)
        if number in d + e + f:
            find_numb_bo4ka(number, d)
            find_numb_bo4ka(number, e)
            find_numb_bo4ka(number, f)
        pas = input("Если ты видишь эту цифру у себя в карточке, то вводи(Y), а если нет, то вводи(N): ")
        if pas == 'Y' and number in a + b + c:
            find_numb_bo4ka(number, a)
            find_numb_bo4ka(number, b)
            find_numb_bo4ka(number, c)
            cycle += 1
        elif pas == 'N' and number not in a + b + c:
            cycle += 1
        elif pas != 'N' or 'Y':
            print("\n Вы ввели другой символ! Точнее с клавиатурой ;-) \n ")

        else:
            print('Вы проиграли')
            break
    elif victory_hum == true_hum:
        print("Вы выиграли")
        break
    elif victory_com == true_com:
        print("Соперник выиграл")
        break






