from math import gcd
from functools import reduce

my_list1 = [24, 36, 48, 60]
my_list2 = [12, 18, 24, 36, 72]
my_list1.extend(my_list2)
result = reduce(gcd, my_list1)
print("наибольший общий делитель двух массивов чисел: " + str(result));