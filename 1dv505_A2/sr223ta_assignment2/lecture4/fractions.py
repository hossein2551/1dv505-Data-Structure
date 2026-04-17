


import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Deviding by zero is not defined")
        
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Deviding by zero is not definied")
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)


f1 = Fraction(3, 4)
f2 = Fraction(2, 5)

print(f"f1: {f1}")
print(f"f2: {f2}")
print("\nCalculations:")
print(f"f1 + f2 = {f1 + f2}")
print(f"f1 - f2 = {f1 - f2}")
print(f"f1 * f2 = {f1 * f2}")
print(f"f1 / f2 = {f1 / f2}")
