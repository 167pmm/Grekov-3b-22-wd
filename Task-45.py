input_file = input("Введите имя файла (с расширением): ")

try:
    file = open(input_file, 'r', encoding='utf-8')
except FileNotFoundError:
    print("Ошибка")
except OSError:
    print("Ошибка")
else:
    text = file.read()
    print(text)
    file.close()