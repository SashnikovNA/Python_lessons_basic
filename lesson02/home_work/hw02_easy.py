# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print("\n Задача 1")
fruits = ['apple', 'banana', 'pineapple', 'marshmellow', 'peach', 'lime', 'kiwi' ]
i = 0
fruit_counter = 1
while len(fruits) > i:
    print("{}){:>15}".format(fruit_counter, fruits[i]))
    i += 1
    fruit_counter +=1



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


print("\n\n\n Задача 2")
first_list = [ 111, 222, 333, 444, 555, 666]
second_list = [ 123, 222, 234, 345, 555, 567]
for numz in first_list:
    if numz in second_list:
        first_list.remove(numz)
print(first_list)



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


print("\n\n\n Задача 3")
random_list = [1,43,44,65,22,5,2,11,22]
new_list = [1,43,44,65,22,5,2,11,22]
i=0
while i < len(random_list):
    if random_list[i] % 2 == 0:
        new_list[i] = random_list[i]/4
    else:
        new_list[i] = random_list[i]*2
    i += 1

print("Исходный список :", random_list)
print("Новый список :", new_list)
