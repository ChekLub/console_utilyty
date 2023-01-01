# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"


import os
import easy


do = {
    "help": easy.print_help,
    "4": easy.make_dir,
    "1": easy.change_dir,
    "3": easy.del_dir,
    "2": easy.list_dir
}

cwd = os.getcwd()

q = 'run'

print("Перейти в папку - нажмите 1, \n Просмотреть содержимое текущей папки - нажмите 2, \n Удалить папку - нажмите 3, \n Создать папку - нажмите 4, \n Для справки - введите help, \n Для завершения работы - введите quit")
q = 'run'
ind = 1
while q != 'quit':
    key = input("Выберите действие: ")
    if key == 'quit':
        q = 'quit'
        exit()

    if '134'.find(key) != -1:
        dir_name = input('Введите имя папки: ')
        if dir_name == '':
            dir_name = 'NewDir'+ str(ind)
            ind += 1

        if do.get(key):
            do[key](dir_name)
        else:
            print("Задан неверный ключ")
    else:
        if do.get(key):
            do[key]()
        else:
            print("Задан неверный ключ")
