import random


class GameLogic:

    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.num3 = None
        self.num4 = None
        self.number = self.generate_number()

    def generate_number(self):
        same_digits = True
        while same_digits:
            self.num1 = str(random.randint(0, 9))
            self.num2 = str(random.randint(0, 9))
            self.num3 = str(random.randint(0, 9))
            self.num4 = str(random.randint(0, 9))
            if self.num1 != self.num2 or self.num1 != self.num3 or self.num1 != self.num4 and self.num2 != self.num3 or \
                    self.num2 != self.num4 and self.num3 != self.num4:
                same_digits = False
        num_as_string = self.num1 + self.num2 + self.num3 + self.num4
        return num_as_string
