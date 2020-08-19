from math import sqrt, sin, cos, exp


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        return ComplexNumber(a+c, b+d)

    def __mul__(self, other):
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        return ComplexNumber(a * c - b * d, b * c + a * d)

    def __sub__(self, other):
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        return ComplexNumber(a - c, b - d)

    def __truediv__(self, other):
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        return ComplexNumber((a * c + b * d) / (c**2 + d**2), (b * c - a * d) / (c**2 + d**2))

    def __abs__(self):
        a = self.real
        b = self.imaginary
        return sqrt(a**2 + b**2)

    def conjugate(self):
        return ComplexNumber(self.real, self.imaginary * -1)

    def exp(self):
        r = round(cos(self.imaginary), 8) * exp(self.real)
        i = round(sin(self.imaginary), 8) * exp(self.real)
        return ComplexNumber(r, i)
