try:
    file = open('test.txt', 'w')
    file.write('Hello, world!\n')
    file.close()
except FileNotFoundError:
    print("Ошибка")
except OSError:
    print("Ошибка")