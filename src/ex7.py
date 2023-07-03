class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.result = 0

    def add(self):
        self.result = self.num1 + self.num2

    def sub(self):
        self.result = self.num1 - self.num2

    def mul(self):
        self.result = self.num1 * self.num2

    def div(self):
        self.result = self.num1 / self.num2

    def get_result(self):
        return self.result


calculator1 = Calculator(4, 3)
calculator1.add()
print(calculator1.get_result())

calculator2 = Calculator(4, 3)
calculator2.sub()
print(calculator2.get_result())

calculator3 = Calculator(2, 3)
calculator3.mul()
print(calculator3.get_result())

calculator4 = Calculator(8, 2)
calculator4.div()
print(calculator4.get_result())
