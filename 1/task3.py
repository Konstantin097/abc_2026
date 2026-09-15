# todo: Данные две переменные:

age = 36.6
temperature = 25

# Нужно обменять значения переменных местами. В итого age
# должен равнятся 25 а temperature – 36.6:

print("Было ", age, " ", temperature)
age, temperature = temperature, age
print("Стало ", age, " ", temperature)

choice = "w"
while choice != "q":
    choice = input("q для выхода ")