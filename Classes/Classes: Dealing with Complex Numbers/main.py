# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        # (a + ib) + (c + id) = (a + c) + i(b + d)
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        # (a + ib) - (c + id) = (a - c) + i(b - d)
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        # (a + ib) * (c + id) = ac + ibc + iad - bd
        return Complex(self.real * no.real - self.imaginary * no.imaginary,
                       self.imaginary * no.real + self.real * no.imaginary)

    def __truediv__(self, no):
        # (a + ib) / (c + id) = [(ac + bd) / (c^2 + d^2)] + i[(bc - ad) / (c^2 + d^2)]
        c2pd2 = no.real ** 2 + no.imaginary ** 2
        return Complex((self.real * no.real + self.imaginary * no.imaginary) / c2pd2,
                       (self.imaginary * no.real - self.real * no.imaginary) / c2pd2)

    def mod(self):
        # mod(a + ib) = (a^2 + b^2)^(1 / 2)
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % self.imaginary
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))

        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
