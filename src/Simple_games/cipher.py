# Шифр Цезаря

SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)


def get_mode():
    while True:
        print('Вы хотите зашифровать, расшифровать взомать текст?')
        mode = input().lower()
        if mode in ['зашифровать', 'з', 'расшифровать', 'р', 'взломать', 'в']:
            return mode
        else:
            print('Введите "зашифровать" или "з" для зашифровки или "расшифровать" \
                  или "р" для расшифровки или "взломать" или "в" для взлома.')


def get_message():
    print('Введите текст:')
    return input()


def get_key():
    while True:
        print('Введите ключ шифрования (1-%s)' % MAX_KEY_SIZE)
        key = int(input())
        if 1 <= key <= MAX_KEY_SIZE:
            return key


def get_translated_message(mode, message, key):
    if mode[0] == 'р':
        key = -key
    translated = ''

    for symbol in message:
        symbol_index = SYMBOLS.find(symbol)
        if symbol_index == -1:
            translated += symbol
        else:
            symbol_index += key

            if symbol_index >= len(SYMBOLS):
                symbol_index -= len(SYMBOLS)
            elif symbol_index < 0:
                symbol_index += len(SYMBOLS)

            translated += SYMBOLS[symbol_index]

    return translated


mode = get_mode()
message = get_message()
if mode[0] != 'в':
    key = get_key()
    print('Преобразованный текст:')
    print(get_translated_message(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, get_translated_message('расшифровать', message, key))