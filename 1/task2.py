#В программе с сначала выводятся типы до преобразования (х.1), 
#а потом после преобразования (х.2)

# todo: 1. Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"
print("1.1 ", type(age), " ", type(foo))
age = int(age)
#foo = int(foo) при попытке привести к числу выдает ошибку,
#т.к. есть буквенная часть; можно попробовать использовать срез,
#чтобы разделить на численную и буквенную части, а затем преобразовать численную
print("1.2 ", type(age), " ", type(foo))

# 2. Преобразуйте переменную age в Boolean
age = "123abc"
print("2.1 ", type(age))
age = bool(age)
print("2.2 ", type(age))

# 3. Преобразуйте переменную flag в Boolean
flag = 1
print("3.1 ", type(flag))
flag = bool(flag)
print("3.2 ", type(flag))

# 4. Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""
print("4.1 ", type(str_one), " ", type(str_two))
str_one = bool(str_one)
str_two = bool(str_two)
print("4.2 ", type(str_one), " ", type(str_two))

# 5. Преобразуйте значение 0 и 1 в Boolean
print("5.1 ", type(0), " ", type(1))
zero = bool(0)
one = bool (1)
print("5.2 ", type(zero), " ", type(one))

# 6. Преобразуйте False в строку
print("6.1 ", type(False))
string = str(False)
print("6.2 ", type(string))

choice = "w"
while choice != "q":
    choice = input("q для выхода ")
