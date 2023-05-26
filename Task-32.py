class Schoolboy:
    def __init__(self, name, classroom):
        self.name = name
        self.classroom = classroom

    def study(self):
        print(f"Я учусь в {self.classroom} классе")


schoolboy = Schoolboy('Иван', 10)
schoolboy.study()