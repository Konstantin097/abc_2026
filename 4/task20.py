#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

# #Содержимое файла inverted_sort.txt:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# # Результат:
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.


#1 Создать список строк
text = [
       "Beautiful is better than ugly.\n",
       "Explicit is better than implicit.\n",
       "Simple is better than complex.\n",
       "Complex is better than complicated.\n"
       ]
#print(text) Проверка


#2 Создать текстовый файл для задания
with open('inverted_sort.txt', 'w') as f:
    for i in text:
        f.write(i)


#3 Список всех строк при помощи метода readlines()
with open('inverted_sort.txt', 'r') as f:
    text_f = f.readlines()
#print(text) Проверка


#4 Список всех строк в обратном порядке
inverted_text = text_f[::-1]
#print(inverted_text) Проверка


#5 Добавление пустой строки для разделения исходного текста и обратного
with open('inverted_sort.txt', 'a') as f:
    f.write('\n')


#6 Запись в конец файла обратного текста  
with open('inverted_sort.txt', 'a') as f:
    for i in inverted_text:
        f.write(i)
 
# choice = "w"
# while choice != "q":
    # choice = input("q для выхода ")