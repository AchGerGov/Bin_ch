print("Двоичный код")
def text_to_binary(text):
    binary_list = []
    for char in text:
        if 'А' <= char <= 'Я':
            position = ord(char) - ord('А') + 1  # Позиция в русском алфавите
        elif 'а' <= char <= 'я':
            position = ord(char) - ord('а') + 1  # Позиция в русском алфавите
        elif 'A' <= char <= 'Z':
            position = ord(char) - ord('A') + 33  # Позиция в английском алфавите (33-58)
        elif 'a' <= char <= 'z':
            position = ord(char) - ord('a') + 33  # Позиция в английском алфавите (33-58)
        else:
            position = 0  # Для неалфавитных символов

        binary_char = format(position, '08b')  # Преобразуем позицию в двоичный код (8 бит)
        binary_list.append(binary_char)
    
    return ' '.join(binary_list)

def binary_to_text(binary_text):
    binary_chars = binary_text.split()  # Разделяем строку по пробелам
    text = ''
    for b in binary_chars:
        position = int(b, 2)  # Десятичное значение
        if 1 <= position <= 32:  # Позиции для русского алфавита
            text += chr(position - 1 + ord('А'))  # Русские буквы
        elif 33 <= position <= 58:  # Позиции для английского алфавита
            text += chr(position - 33 + ord('A'))  # Английские буквы
        else:
            text += '?'  # Непознанный символ

    return text

# Пример использования
if __name__ == "__main__":
    while True:
        choice = input("Введите 'E' для шифрования или 'D' для дешифровки (или '***' для выхода): ").upper()
        
        if choice == "***":
            print("Выход из программы.")
            break

        if choice == 'E':
            message = input("Введите сообщение для шифрования: ")
            binary_message = text_to_binary(message)
            print("Зашифрованное сообщение (двоичный код):", binary_message)
        
        elif choice == 'D':
            binary_message = input("Введите двоичный код для дешифровки: ")
            decrypted_message = binary_to_text(binary_message)
            print("Расшифрованное сообщение:", decrypted_message)

        else:
            print("Недопустимый выбор. Пожалуйста, попробуйте снова.")
