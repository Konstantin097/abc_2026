#todo: Допишите для игры "Поле чудес" функции сохранения и загрузки игры через сериализацию.
# Данные сериализации записываются и сохраняются в файле.

import  random
import json


print('В процессе игры вводите save для сохранения и load для загрузки')


_dict = {'False': 'Логическое значение',
         'None': 'Пустой', 
         'Пирамида': 'Древнее египетское сооружение', 
         'Космонавт': 'Летает в космос', 
         'Солнце': 'Желтая звезда'}
keys = list(_dict.keys())
ind = random.randint(0, len(keys) - 1)
secret = keys[ind]
mask = [' * '] * len(secret)
# Проверяем сколько у нас уже есть сохранений
with open('saves.txt', 'r') as f:
    lines = f.readlines()
if len(lines) == 0:
    save_count = 0
else:
    save_count = len(lines)


def save_game(s, m):
    """ Сохраняет игру  """
    global save_count
    save_count += 1
    inf = {'secret': s,
           'mask': m
          }
    with open(f'save_{save_count}.json', 'w') as f:
            json.dump(inf, f)
    with open('saves.txt', 'a') as f:
        f.write(f'save_{save_count}.json' + '\n')
    

def load_game():
    """ Загружает игру  """
    with open('saves.txt', 'r') as f:
        saves = f.read()
    print(saves)
    number = int(input('Выберите номер нужного сохранения: '))
    with open(f'save_{number}.json', 'r') as f:
        inf = json.load(f)
    global secret
    global mask
    secret, mask = tuple(inf.values())
    

def show_describe():
    """ Выводит описание слова  """
    print(_dict[secret])


def show_secret():
    """ Выводит слово """
    for val in mask:
       print(val, end="")


def get_letter():
    letter = input("\n Введите букву: ")
    return letter


def check_letter(letter):
    if letter == 'save':
        save_game(secret, mask)
    elif letter == 'load':
        load_game()
    for ind, val in enumerate(secret):
        if val.upper() == letter.upper():
            mask[ind] = f" {letter} "
    
    
def start():
    while ( " * " in mask):
        show_describe()
        show_secret()
        letter = get_letter()
        check_letter(letter)
    else:
        show_secret()


start()
