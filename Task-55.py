try:
    numbers = input("Введите список целых чисел через запятую: ")
    myList = numbers.split(",")
    myList1 = [int(x) for x in myList]
    myList1.sort()
    print("Минимальное число в списке: " + str(myList1[0]))

except ValueError:
    print("Ошибка. Введены не целые числа")