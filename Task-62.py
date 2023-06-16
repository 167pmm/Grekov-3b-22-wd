class Robot:
    def __init__(self, name, speed):
        self.name = name               #

    def movement(self, time):
        traveled = time * self.speed
        return print(f"Робот {self.name} пройдет {traveled} км за {time} ч, при скорости {self.speed} км/ч")


class CrawlerRobot(Robot):
    def __init__(self, territory, name, speed):
        super().__init__(name, speed)
        self.territory = territory     # Аттрибут Территория

    def movement(self, time):
        traveled = time * self.speed
        return print(f"Робот {self.name} пройдет {traveled} км по {self.territory} за {time} ч,"
                     f" при скорости {self.speed} км/ч")


class RobotOnWheels(Robot):
    def __init__(self, model, name, speed):
        super().__init__(name, speed)
        self.model = model

    def movement(self, time):
        traveled = time * self.speed
        return print(f"Робот {self.name} марки {self.model} пройдет {traveled} км за {time} ч,"
                     f" при скорости {self.speed} км/ч")


Robot1 = Robot('Chappy', 21)
Robot1.movement(5)

CrawlerRobot1 = CrawlerRobot('Аляска', 'Счастливчик', 20)
CrawlerRobot1.movement(3)

RobotOnWheels1 = RobotOnWheels('Lada', 'Бедолага', 10)
RobotOnWheels1.movement(2)