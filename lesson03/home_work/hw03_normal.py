# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n,m):
  start = n
  i = 1
  fib_list = []
  fib_list.append(start)
  #Начинаем заполнение ряда с начального ввода пользователя
  while start < m:
    start +=i
    fib_list.append(start)
    i = sum(fib_list[-2:])
    #Исполняем основное условие ряда - последующий член равен сумме 2х предыдущих
    if i <= m:
      fib_list.append(i)
  print ("Ряд Фибоначи :", fib_list)

fibonacci(0, 777)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

# Сортировка Шелла
# Идея заключается в том, чтобы просматривать элементы беря каждый i тый элементы(начало откуда угодно). В результате мы получаем массив где каждый i-тый элемент отсортирован. Повторяя такую операцию с использованием меньших i, заканчивая 1 результатом будет отсортированный массив.

def Shell_sort(sort_list):
    t = int(len(sort_list)/2)
    while t > 0:
        for i in range(len(sort_list)-t):
            j = i
            while j >= 0 and sort_list[j] > sort_list[j+t]:
                sort_list[j], sort_list[j+t] = sort_list[j+t], sort_list[j]
                j -= 1
        t = int(t/2)
        pass
    print(sort_list)

Shell_sort([2, 10, -12, 66, 20, -13, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

