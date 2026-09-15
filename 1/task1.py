# todo: Определить в коде переменные:
# 1. Целочисленного типа
# 2. Вещественного типа
# 3. Логического типа
# 4. Строкового типа
# 5. Пустого типа
# Вывести их типы.
int_var = 123
float_var = 123.0
bool_var = True
str_var = "123"
null_var = None
print("int_var: ", int_var, " - ", type(int_var))
print("float_var: ", float_var, " - ", type(float_var))
print("bool_var: ", bool_var, " - ", type(bool_var))
print("str_var: ", str_var, " - ", type(str_var))
print("null_var: ", null_var, " - ", type(null_var))

choice = "w"
while choice != "q":
    choice = input("q для выхода ")