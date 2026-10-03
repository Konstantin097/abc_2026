#todo: Напишите лямбду функцию которая возвращает максимальное число
# из 2 переданных чисел


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
(lambda a, b: print(a) if (a >= b) else print(b))(a, b)


#todo: Для каждого значения из списка mass получите
# список проверок(True или False) вхождений значений в диапазон от 1 до 130
mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]
print(list(filter(lambda i:  ((1 <= i) and (i <= 130)),  mass)))


#todo: Отсортируйте список с помощью функции filter()
# и получите итоговый список только нечетных значений
list_ = [ 10, 11, 14, 25, 33, 36, 100, 101 ]
print(list(filter(lambda val:  val%2 != 0,  list_ )))


#todo: Отсортируйте список по расширению ".mp3"
files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']
print(list(filter(lambda j: j.split('.')[-1] == "mp3",  files)))


choice = 'w'
while choice != 'q':
    choice = input('Введите q для выхода: ')
