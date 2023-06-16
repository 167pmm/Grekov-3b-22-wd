import os.path


class ToDoList(object):

    def __init__(self):
        self.list = []

        if os.path.isfile('output.txt'):
            with open('output.txt') as f:
                self.list = list(f)
        else:
            MyFile = open('output.txt', 'w')
            MyFile.close()
        pass

    def addElement(self, element):
        self.list.append(element)
        self.save()
        pass

    def removeElement(self, element):
        self.list.remove(element)
        self.save()
        pass

    def save(self):
        MyFile = open('output.txt', 'w')
        for element in self.list:
            MyFile.write(element)
            MyFile.write('\n')
        MyFile.close()
        pass

    def display(self):
        print(' '.join(str(el) for el in self.list))
        pass

# myList = ToDoList()
# myList.addElement("Завтрак")
# myList.addElement("Домашнее задание")
# myList.addElement("Ужин")
# myList.removeElement("Ужин")
# myList.display()