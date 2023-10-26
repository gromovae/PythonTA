"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""


class Order:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self):
        if self.discount_strategy is not None:
            return int(self.discount_strategy.set_discount(self.price))
        return self.price


class Strategy:
    def set_discount(self, price):
        pass


class MorningDiscount(Strategy):
    def set_discount(self, price):
        price = price * 0.5
        return price


class ElderDiscount(Strategy):
    def set_discount(self, price):
        price = price * 0.1
        return price


class StudentDiscount(Strategy):
    def set_discount(self, price):
        price = price * 0.25
        return price


morning_discount = MorningDiscount()
elder_discount = ElderDiscount()
student_discount = StudentDiscount()

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50
order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
order_3 = Order(100, student_discount)
assert order_3.final_price() == 25
order_4 = Order(100)

print(order_1.final_price(), order_2.final_price(), order_3.final_price(), order_4.final_price())
