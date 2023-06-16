try:
    number = int(input("Введите целое число: "))
    sum = 0
    for i in range(1, number + 1):
        sum+=i
    print("Сумма: "+str(sum))

except ValueError:
    print("Ошибка. Введено не целое число")