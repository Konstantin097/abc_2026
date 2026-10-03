#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу:
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.


crypt_text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

for i in range(1, 26):
    decrypt_text = ""
    for j in range(len(crypt_text)):
        # Если это английский символ
        if ((97 <= ord(crypt_text[j])) and (ord(crypt_text[j]) <= 122)):
            # Если не надо возвращаться в начало алфавита
            if (122 - ord(crypt_text[j])) >= i:
                decrypt_text = decrypt_text + chr(ord(crypt_text[j]) + i)
            # Если надо возвращаться в начало алфавита
            else:
                decrypt_text = decrypt_text + chr(97 + (i - (122 - ord(crypt_text[j]))) - 1)
        else:
            decrypt_text = decrypt_text + chr(ord(crypt_text[j]))
    print(decrypt_text)
#although that way may not be obvious at first unless you're dutch.
#хотя поначалу этот способ может быть неочевиден — разве что вы голландец.

choice = 'w'
while choice != 'q':
    choice = input('Введите q для выхода: ')