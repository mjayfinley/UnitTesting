class Calculator:
    def __init__ (self,input_1,input_2):
        self.input_1 = input_1
        self.input_2 = input_2

    def add(self):
        return self.input_1 + self.input_2

    def subtract(self):
        return self.input_1 - self.input_2

    def multiply(self):
        return self.input_1 * self.input_2

    def divide(self):
        return self.input_1 / self.input_2

calculator = Calculator(4,4)

print(calculator.add())
print(calculator.subtract())
print(calculator.multiply())
print(calculator.divide())
