#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

# В "0 23 15 18 12 4 !" по всей видимости лишний "0"; цифр 6, а букв 5


#Считываем строки
with open('input.txt', 'r') as f:
    strings = f.readlines()
# print(strings)


#Убираем пробелы
text = list([[j for j in i.split()] for i in strings])
# print(text)


new_text = list([[(chr(ord('a') + int(j) - 1)) if j.isdigit() else j for j in i ] for i in text])
# print(new_text)


# Запись в файл
with open('output.txt', 'w') as f:
    # построчная печать в файл
    for i in new_text:
        for j in i:
            f.write(j)
        # по завершению одной строки переходим на новую строку
        f.write('\n')