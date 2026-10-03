#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)

# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36

# Требуется написать функцию load_matrix(filename), которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.

# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

def load_matrix(filename):
    # Считываем строки
    with open(filename, 'r') as f:
        matrix = f.readlines()

    # Убираем пробелы
    matrix = list([[j for j in i.split()] for i in matrix])

    # Смотрим количество элементов в каждой строке для дальнейшей проверки
    k = list([[len(i)] for i in matrix])
    
    #Проверка 
    if k.count(k[0]) == len(k):
        return list([i for i in matrix])
    else:
        return False

print(load_matrix('matrix.txt'))


choice = 'w'
while choice == 'w':
    choice = input('Введите любую клавишу для выхода: ')