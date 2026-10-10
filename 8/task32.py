# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.

# Пример использования
# user = User("test@example.com", "secret")
# print(user.email)  # test@example.com
# # print(user.password) # AttributeError
# print(user.check_password("secret"))  # True
# print(user.check_password("wrong"))   # False


class User:
    def __init__(self, email, password):
        self.__email = email
        self.__password = hash(password)
    
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, new_email):
        if '@' in new_email:
            self.__email = new_email
        else:
            print("Некорректный email: должен содержать символ @")

    #Для возможности изменения пароля, сеттер не работает без property
    @property
    def password(self):
        raise AttributeError
    @password.setter
    def password(self, new_password):
        self.__password = hash(new_password)


    def check_password(self, password):
        return self.__password == hash(password)

    
user = User("test@example.com", "secret")
print(user.email)  # test@example.com
#Проверка валидации
user.email = 'testexample.com'
#print(user.password) # AttributeError
print(user.check_password("secret"))  # True
print(user.check_password("wrong"))   # False
#Проверка изменения пароля
user.password = "wrong"
print(user.check_password("secret"))  # False
print(user.check_password("wrong"))   # True


choice = 'w'
while choice == 'w':
    choice = input('Введите любую клавишу, чтобы выйти: ')
