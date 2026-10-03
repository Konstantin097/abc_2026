from helpers.io import logger
from helpers.crypt import caesar_cipher

# Настраиваем логгер
log = logger("test_app")

# Тест логгера
log.info("Логгер работает!")

# Тест шифра Цезаря
original = "Hello, World!"
encrypted = caesar_cipher(original, shift=3)
decrypted = caesar_cipher(encrypted, shift=3, decode=True)

log.info(f"Оригинал:    {original}")
log.info(f"Зашифровка:  {encrypted}")
log.info(f"Расшифровка: {decrypted}")

# Проверка корректности
assert decrypted == original, "Расшифровка не совпала с оригиналом!"
log.info("Все тесты пройдены ✓")