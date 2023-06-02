input_number = input("Введите число: ")
try:
    arg = int(input_number)
except ValueError:
    print("Ошибка")
else:
    print(arg * arg)