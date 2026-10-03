def caesar_cipher(text, shift=3, decode=False):
    """
    Шифр Цезаря: сдвиг букв на shift позиций по алфавиту.
    Регистр сохраняется, не-буквы остаются без изменений.
    decode=True — расшифровка (сдвиг в обратную сторону).
    """
    if decode:
        shift = -shift

    result = []
    for char in text:
        if "a" <= char <= "z":
            base = ord("a")
            result.append(chr((ord(char) - base + shift) % 26 + base))
        elif "A" <= char <= "Z":
            base = ord("A")
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)

    return "".join(result)
