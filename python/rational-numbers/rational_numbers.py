from fractions import Fraction as F


class Rational(object):

    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.reduce()

    def reduce(self):
        for i in range(min(abs(self.numer), abs(self.denom)), 1, -1):
           if self.numer % i == 0 and self.denom % i == 0:
               self.numer = int(self.numer / i)
               self.denom = int(self.denom / i)
        if self.numer == 0:
           self.denom = 1
        if self.denom < 0 and self.numer >= 0:
           self.denom = abs(self.denom)
           self.numer = -1 * self.numer
        elif self.denom < 0 and self.numer < 0:
            self.denom = self.denom * (-1)
            self.numer = self.numer * (-1)

    def __str__(self):
        return "Numer:{}, Denominator{}".format(self.numer, self.denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        res = F(self.numer, self.denom) + F(other.numer, other.denom)
        return Rational(res.numerator, res.denominator)

    def __sub__(self, other):
        res = F(self.numer, self.denom) - F(other.numer, other.denom)
        return Rational(res.numerator, res.denominator)

    def __mul__(self, other):
        res = F(self.numer, self.denom) * F(other.numer, other.denom)
        return Rational(res.numerator, res.denominator)

    def __truediv__(self, other):
        res = F(self.numer, self.denom) / F(other.numer, other.denom)
        return Rational(res.numerator, res.denominator)

    def __abs__(self):
        res = abs(F(self.numer, self.denom))
        return Rational(res.numerator, res.denominator)

    def __pow__(self, power):
        res = F(self.numer, self.denom) ** power
        return Rational(res.numerator, res.denominator)

    def __rpow__(self, base):
        return base ** F(self.numer, self.denom)
