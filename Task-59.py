myList = ["apple", "orange", "banana", "pineapple", "grape"]
myList = sorted(myList, key=len)
myList.reverse()
print("Отсортировать в порядке убывания длины строк: ",  myList)