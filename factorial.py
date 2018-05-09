class Factorial:
    def __init__ (self,number):
        self.number = number

    def calc_factorial(self):
        if self.number == 0:
            return 1
        else:
            temp_n = self.number
            self.number -= 1
            return temp_n * self.calc_factorial()



find_factorial = Factorial(5)

print(find_factorial.calc_factorial())
