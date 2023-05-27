try:
    file = open('text.txt', 'r')
    print(file.read())
    file.close()
except FileNotFoundError:
    print('Файл не найден')
finally:
    print('\nЗавершение программы')