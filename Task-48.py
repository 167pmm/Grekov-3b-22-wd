from statistics import mean

my_list = [5, 7, 11, 13, 15, 20, 25]
my_list_mid = []

for i in range(len(my_list)):
    if my_list[i]>10:
        my_list_mid.append(my_list[i])

sum = mean(my_list_mid)
print("Среднее арифметическое элементов массива, которые больше 10: "+str(sum))