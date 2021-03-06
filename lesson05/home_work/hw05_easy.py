# Выполнил: Сашников Никита Александрович


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

print(os.getcwd())
os.chdir(os.getcwd())
print(os.chdir(os.getcwd()))

#Якобы ход выше должен вернуть нас из странного места в то, где открыт скрипт :-)

#Задаю 2 функции (создание и удаление). т.к. в задании четко сказано про 9 папок,
# то не предлагаю пользователю ввести количество, а зашиваю в функции

def create_new_dir(dirname):
    for i in range (1,10):
        try:
            os.mkdir(str(dirname + str(i)))
        except FileExistsError:
            print("каталог существует")
        
def remove_dir(dirname):
    for i in range (1,10):
        try:
            os.rmdir(str(dirname + str(i)))
        except FileNotFoundError:
            print(dirname + ' - каталога не существует')


# а ниже уже бодренький терминал, беседующий с пользователем Х-)

while True:


    ask = input("Что ты хочешь сделать, друг мой? \n  \
    1 - создать папки \n  \
    2 - удалить папки \n \
    q - убежать отсюда \n ")
                
    if ask == "1":
        create_new_dir("Папулечки_")
    elif ask == "2":
        remove_dir("Папулечки_")
    elif ask == "q":
        break
    else:
        print("Что-то ты не то нажал :-)")



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


# Выводим названия файлов/папок в удобоваримом виде (список построчно)
def list_of_dir():
    dirs = []
    i = 0
    print("Список папок/файлов текущего местоположения :")
    for l in os.listdir():
        if os.path.isdir(l):
            i += 1
            print(i,l)
    return 0
 # Проверяем работу:
 
print(os.getcwd())
list_of_dir()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
from shutil import copyfile

def copy_this_file():
    src = str(sys.argv[0]) #текущий полный путь к скрипту или к названию файла
    dst = src.replace('.py','_copy.py') #добавляем в имя файла слово "Копия", иначе будет печаль
    copyfile(src, dst) #копирует содержимое (но не метаданные) файла src в файл dst
    
 # Проверяем работу функции:
copy_this_file()

