try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    result = a / b
    print(result)
except Exception:
    print('Ошибка')
finally:
    print('\nЗавершение программы')