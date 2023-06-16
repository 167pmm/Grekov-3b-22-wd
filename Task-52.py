my_list1 = [1, 2, 3, 2, 1]
my_list2 = my_list1.copy()
my_list2.reverse()
if my_list1 == my_list2:
    print("массив является палиндромом")
else:
    print("массив не является палиндромом")