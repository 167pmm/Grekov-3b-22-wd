class Card:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def count_change(self, amount):
        if self.count >= amount:
            self.count -= amount
        else:
            print('Amount change error')
            exit()

    def price_change(self, price_change):
        if self.price >= price_change:
            self.price -= price_change
        else:
            print('Price change error')
            exit()


good = Card('Maxibon', 150, 4)
good.count_change(4)
good.price_change(149)