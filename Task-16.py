class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print("Кошка по имени {}, {} лет, цвет {}".format(self.name, self.age, self.color))


my_cat = Cat("Клеопатра", 11, "Телесный")
my_cat.info()