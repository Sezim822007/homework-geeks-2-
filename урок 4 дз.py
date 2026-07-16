rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    # Конвертация в сомы
    def convert_to_kgs(self):
        return self.amount * rates[self.currency]

    # Сложение денег
    def __add__(self, other):
        total_kgs = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(total_kgs, "KGS")

    # Вычитание денег
    def __sub__(self, other):
        result_kgs = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(result_kgs, "KGS")

    # Умножение на число
    def __mul__(self, number):
        return Money(self.amount * number, self.currency)

    # Деление на число
    def __truediv__(self, number):
        return Money(self.amount / number, self.currency)

    # Вывод
    def __str__(self):
        return f"{self.amount} {self.currency}"


# Проверка работы

money1 = Money(100, "USD")
money2 = Money(5000, "KGS")

result = money1 + money2

print(result)

print(money1 - money2)

print(money1 * 3)

print(money2 / 2)