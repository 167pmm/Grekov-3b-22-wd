import random


class Character:
    def __init__(self, name, level, health, attack, protection):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.protection = protection
        self.damaged = self.health

    def hit(self):
        return random.randint(1, self.attack)

    def damage(self, quantity):
        damage = quantity - (self.protection * 10 / 100)
        self.damaged -= damage
        if self.damaged <= 0:
            print(f'Персонаж {self.name} получает урон {damage}, персонаж убит')
            return True
        else:
            print(f'Персонаж {self.name} получает урон {damage}, осталось здоровья {self.damaged}')
            return False

    def healing(self):
        self.damaged = self.health

    def level_up(self):
        self.level += 1
        self.health += round((self.health * 10) / 100)
        self.attack += round((self.attack * 10) / 100)
        print(f'Уровень персонажа {self.name} повышен до {self.level}. Здоровье увеличено до {self.health},'
              f' атака увеличена до {self.attack}')


Character1 = Character('Char1', 1, 100, 10, 10)
Character2 = Character('Char2', 1, 100, 10, 10)

count1 = 0
count2 = 0
for i in range(3):
    ret = True
    while ret:
        if Character1.damage(Character2.hit()):
            print(f'Раунд {i+1}. Победитель {Character2.name}')
            Character2.level_up()
            count2 += 1
            ret = False
        elif Character2.damage(Character1.hit()):
            print(f'Раунд {i+1}. Победитель {Character1.name}')
            Character1.level_up()
            count1 += 1
            ret = False
    Character1.healing()
    Character2.healing()

if count1 > count2:
    print(f'>>> Побеждает {Character1.name}')
else:
    print(f'>>> Побеждает {Character2.name}')