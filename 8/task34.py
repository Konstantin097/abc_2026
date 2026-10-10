# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.

# Пример использования
# book = Product("Book", 10)
# pen = Product("Pen", 2)
# order = Order()
# order.add_product(book)
# order.add_product(pen)
# print(f"Общая стоимость: {order.total_price}")  # 12
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        if price < 0:
            self.__price = 0
        else:
            self.__price = price
  
class Order:
    def __init__(self):
        # список товаров в заказе
        self._products = []

    def add_product(self, product):
        """Добавить товар в заказ."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только экземпляры Product")
        self._products.append(product)

    def remove_product(self, product):
        """Удалить товар из заказа (удаляет первое совпадение)."""
        if product in self._products:
            self._products.remove(product)
        else:
            # можно либо ничего не делать, либо выбросить ошибку — тут просто игнорируем
            pass

    @property
    def total_price(self):
        """Вычисляемое свойство: общая стоимость всех товаров в заказе."""
        return sum(p.price for p in self._products)
        

book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(f"Общая стоимость: {order.total_price}")  # 12


choice = 'w'
while choice == 'w':
    choice = input('Введите любую клавишу, чтобы выйти: ')