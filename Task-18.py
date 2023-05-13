class Figure:

    def __init__(self, square, perimeter):
        self.square = square
        self.perimeter = perimeter

    def info(self):
        print("Площадь - {}, Периметр - {}".format(self.square, self.perimeter))


figure = Figure(11, 19)
figure.info()