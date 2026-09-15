# В восточном календаре принят 60-летний цикл, состоящий из 12- летних подциклов,
# обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный.
# В каждом подцикле годы носят названия животных: крысы, коровы, тигра, зайца, дракона,
# змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи. По номеру года вывести его название,
# если 1984 год был началом цикла — годом зеленой крысы.
year = int(input("Введите год (1900 - 2043): "))
while ((year < 1900) or (2043 < year)):
    year = int(input("Введите год (1900 - 2043): "))

animals = ["Крыса", 
           "Бык",
           "Тигр", 
           "Кролик", 
           "Дракон", 
           "Змея", 
           "Лошадь", 
           "Коза", 
           "Обезьяна", 
           "Петух", 
           "Собака", 
           "Свинья"]

colors = ["Белый", 
          "Черный",
          "Зеленый", 
          "Красный", 
          "Желтый"]

color = {}
count_color = 0

animal = {}
count_animal = 0

for y in range(1900, 2044, 2):
    if count_color < len(colors):
        color[y] = color[y+1] = colors[count_color]
        count_color += 1
    else:
        count_color = 0
        color[y] = color[y+1] = colors[count_color]
        count_color += 1

for y in range(1900, 2044):
    if count_animal < len(animals):
        animal[y] = animals[count_animal]
        count_animal += 1
    else:
        count_animal = 0
        animal[y] = animals[count_animal]
        count_animal += 1

print("Год:", year, "\nЦвет:", color[year], "\nЖивотное:", animal[year])

choice = "w"
while choice != "q":
    choice = input("q для выхода ")