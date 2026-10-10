# Инкапсуляция и property
# todo: Класс "Температура"
# Создайте класс Temperature, который хранит температуру в градусах Цельсия.
# Добавьте свойство для получения и установки температуры в Фаренгейтах и Кельвинах.
# Внутренне температура должна храниться только в Цельсиях.

# celsius (get, set) - работа с Цельсиями.
# fahrenheit (get, set) - при установке конвертирует значение в Цельсии.
# kelvin (get, set) - при установке конвертирует значение в Цельсии.

# Пример использования
# t = Temperature(25)
# print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
# t.fahrenheit = 32
# print(f"После установки 32F: {t.celsius}C")


class Temperature:
    def __init__(self, temp):
        self.__celsius = temp
   

   # Для Цельсия
    @property
    def celsius(self):
        return self.__celsius
    @celsius.setter
    def celsius(self, celsius):
        self.__celsius = celsius
    
    # Для Фаренгейта
    @property
    def fahrenheit(self):
        return self.__celsius * 1.8 + 32
    @fahrenheit.setter
    def fahrenheit(self, fahrenheit):
        self.__celsius = (fahrenheit - 32) / 1.8
   

   # Для Кельвина
    @property
    def kelvin(self):
        return self.__celsius + 273.15
    @kelvin.setter
    def kelvin(self, kelvin):
        self.__celsius = kelvin - 273.15


t = Temperature(25)
print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
t.fahrenheit = 32
print(f"После установки 32F: {t.celsius}C")


choice = 'w'
while choice == 'w':
    choice = input('Введите любую клавишу, чтобы выйти: ')