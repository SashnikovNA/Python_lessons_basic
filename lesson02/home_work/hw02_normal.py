# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

print("\n Задача-1 \n")
import math
start_list = [3, 9, 25, -342, -2, 45, 1, 0]
sqrt_list = []
int_sqrt_list = []
for i in start_list:
    if i > 0:
      sqrt_i = math.sqrt(i)
      sqrt_list.append(sqrt_i)
for j in sqrt_list:
  if (j).is_integer():
    int_sqrt_list.append(int(j))
 
print("Исходный список ", start_list)   
print("Итоговый список целых корней :",int_sqrt_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print("\n Задача-2 \n")
date = input("Введите дату в формате dd.mm.yyyy : ")

date_list = date.split('.')
#date_list = [ i.lstrip('0') for i in date_list ]
#интересный метод .strip для отброса нуля, но... я решил пойти другим путём :-)) - использовать словари
str_date_list = []
# print(date_list) #проверка создаваемого списка

day_voc = {
  "01": "Первое",
  "02":"Второе", 
  "03":"Третье",
  "04":"Четвертое",
  "05":"Пятое",
  "06": "Шестое",
  "07":"Седьмое",
  "08":"Второе",
  "09":"Девятое",
  "10":"Десятое",
  "11":"Одиннадцатое", 
  "12":"Двенадцатое",
  "13":"Тринадцатое",
  "14":"Четырнадцатое",
  "15":"Пятнадцатое",
  "16":"Шестнадцатое",
  "17": "Семнадцатое",
  "18":"Восемнадцатое",
  "19":"Девятнадцатое",
  "20":"Двадцатое",
  "21": "Двадцать первое",
  "22":"Двадцать второе",
  "23":"Двадцать третье",
  "24":"Двадцать четвертое",
  "25":"Двадцать пятое",
  "26":"Двадцать шестое",
  "27":"Двадцать седьмое",
  "28":"Двадцать восьмое",
  "29":"Двадцать девятое",
  "30":"Тридцатое",
  "31":"Тридцать первое"}

month_voc = {
  "01": "января",
  "02":"февраля", 
  "03":"марта",
  "04":"апреля",
  "05":"мая",
  "06":"июня",
  "07":"июля",
  "08":"августа",
  "09":"сентября",
  "10":"октября",
  "11":"ноября", 
  "12":"декабря"}
  
day = day_voc[date_list[0]]
month =month_voc[date_list[1]]
year = date_list[2]

print("Введенная дата:", day, month, year," года")

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


print("\n Задача-3 \n")
import random
import math

n = int(input("Введите количество элементов в списке: "))
int_random_list=[] 
for i in range(n):
  int_random_list.append(random.randint(-100, 100))
print(int_random_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print("\n Задача-4 \n")
print(" Не успел :-( ")
